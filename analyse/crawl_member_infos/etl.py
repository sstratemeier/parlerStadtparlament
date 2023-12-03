import os
import pathlib
import logging
import requests
import pandas as pd
from bs4 import BeautifulSoup


def extract_personal_info(soup):
    # Dictionary to hold personal information
    personal_info = {
        'Adresse': '',
        'PLZ / Ort': '',
        'Telefon Geschäft': '',
        'Fax Geschäft': '',
        'E-Mail': '',
        'Beruf': '',
        'Jahrgang': '',
        'Partei': '',
        'Fraktion': ''
    }

    # Find the table containing personal information
    info_table = soup.find('table')
    if info_table:
        rows = info_table.find_all('tr')
        for row in rows:
            col_1 = row.find('th')
            col_2 = row.find('td')
            if col_1 and col_2:
                label = col_1.get_text(strip=True)
                value = col_2.get_text(strip=True)
                if label in personal_info:
                    personal_info[label] = value
    return list(personal_info.values())


def extract_memberships(soup):
    table = soup.find('table', {'summary': "Mitgliedschaften"})
    if table:
        rows = table.find_all('tr')
        data = []
        for row in rows[1:]:
            cols = [ele.text.strip() for ele in row.find_all('td')]
            data.append(cols)
    return data


def extract_vorstoesse(soup):
    table = soup.find('table', {'summary': "Vorstösse"})
    if table:
        rows = table.find_all('tr')
        data = []
        for row in rows[1:]:
            cols = [ele.text.strip() for ele in row.find_all('td')]
            vorstoss_link = row.find('a', href=True)
            geschaeft_guid = vorstoss_link['href'].split('geschaeftGUID=')[1]
            cols.append(geschaeft_guid)
            data.append(cols)
    return data


def access_member_url(name_link):
    # Get personal information
    personal_info_url = 'https://www.stadt.sg.ch' + name_link['href']
    personal_info_response = requests.get(personal_info_url)
    personal_info_soup = BeautifulSoup(personal_info_response.content, 'html.parser')
    personal_info_values = extract_personal_info(personal_info_soup)
    # Get membership information
    membership_info_values = extract_memberships(personal_info_soup)
    # Get Vorstösse information
    vorstoesse_info_values = extract_vorstoesse(personal_info_soup)

    return personal_info_values, membership_info_values, vorstoesse_info_values


def scrape_page(page_nr):
    logging.info(f'Scraping page {page_nr}...')
    url = (f'https://www.stadt.sg.ch/home/verwaltung-politik/demokratie-politik/'
           f'stadtparlament/mitglieder/alleMitglieder.html.viewpage__{page_nr}.html')
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table')
    rows = table.find_all('tr')
    members_data = []
    memberships_data = []
    vorstoesse_data = []
    for row in rows[1:]:  # Skip the header row
        cols = row.find_all('td')
        member_data = [ele.text.strip() for ele in cols]
        member_name = member_data[0]
        logging.info(f'Accessing personal info of {member_name}...')
        name_link = row.find('a', href=True)
        # Check if member is current based on 'Austritt' column being empty
        current_member = member_data[-1] == ''
        if name_link:
            # Fetch and save member image
            person_guid = name_link['href'].split('personGUID=')[1]
            image_url = (f"https://www.stadt.sg.ch/content/stsg/home/verwaltung-politik/demokratie-politik/"
                         f"stadtparlament/mitglieder/alleMitglieder.{person_guid}.spImage")
            image_response = requests.get(image_url)
            if image_response.status_code == 200 and image_response.content:
                # Prepare file path
                file_name = person_guid + '.jpg'
                pictures_path = os.path.join(pathlib.Path(__file__).parents[0], 'data', 'pictures_guid')
                os.makedirs(pictures_path, exist_ok=True)
                file_path = os.path.join(pictures_path, file_name)

                # Save the image
                with open(file_path, 'wb') as file:
                    file.write(image_response.content)

            member_data.append(person_guid)
            personal_info_values, membership_info_values, vorstoesse_info_values = access_member_url(name_link)
            member_data += personal_info_values
            membership_data = [[member_name, person_guid] + membership_info for membership_info in membership_info_values]
            vorstoss_data = [[member_name, person_guid] + vorstoss_info for vorstoss_info in vorstoesse_info_values]
        else:
            member_data += [''] * 10
            membership_data = [[member_name, ''] + [''] * 4]
            vorstoss_data = [[member_name, ''] + [''] * 5]

        members_data.append(member_data)
        memberships_data += membership_data
        vorstoesse_data += vorstoss_data

    return pd.DataFrame(members_data), pd.DataFrame(memberships_data), pd.DataFrame(vorstoesse_data)


def main():
    df_members = pd.DataFrame()
    df_memberships = pd.DataFrame()
    df_vorstoesse = pd.DataFrame()
    for page_nr in range(25):
        df_page_members, df_page_memberships, df_page_vorstoesse = scrape_page(page_nr)
        df_members = pd.concat([df_members, df_page_members], ignore_index=True)
        df_memberships = pd.concat([df_memberships, df_page_memberships], ignore_index=True)
        df_vorstoesse = pd.concat([df_vorstoesse, df_page_vorstoesse], ignore_index=True)
    df_members.columns = ['Name', 'Funktion', 'Partei', 'Eintritt', 'Austritt', 'PersonGUID',
                          'Adresse', 'PLZ / Ort', 'Telefon Geschäft', 'Fax Geschäft',
                          'E-Mail', 'Beruf', 'Jahrgang', 'Partei', 'Fraktion']
    df_members = df_members[['Name', 'Funktion', 'Partei', 'Eintritt', 'Austritt',
                             'PersonGUID', 'Beruf', 'Jahrgang', 'Partei', 'Fraktion']]
    df_memberships.columns = ['Name', 'PersonGUID', 'Gremium', 'Funktion', 'Von', 'Bis']
    df_vorstoesse.columns = ['Name', 'PersonGUID', 'Titel', 'Typ', 'Eröffnung', 'Abschluss', 'GeschäftGUID']

    df_members.to_csv(os.path.join(pathlib.Path(__file__).parents[0], 'data', 'mitglieder.csv'), index=False)
    df_memberships.to_csv(os.path.join(pathlib.Path(__file__).parents[0], 'data', 'mitgliedschaften.csv'), index=False)
    df_vorstoesse.to_csv(os.path.join(pathlib.Path(__file__).parents[0], 'data', 'vorstoesse.csv'), index=False)


'''
def get_traktanden(path_trakt):
    logging.info(f'Downloading Gebäudeeingänge from ods to file {path_trakt}...')
    r = requests.get(f'https://daten.sg.ch/api/records/1.0/download?dataset=traktandierte-geschaefte-sitzungen-stadtparlament-stgallen%40stadt-stgallen')
    with open(path_trakt, 'wb') as f:
        f.write(r.content)
    return path_trakt
'''

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logging.info('Start scraping...')
    main()
    logging.info('... finished scraping.')
