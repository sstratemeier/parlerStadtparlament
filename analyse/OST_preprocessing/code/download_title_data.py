__doc__="""
Skript, welches die Datei 
traktandierte-geschaefte-sitzungen-stadtparlament-stgallen.csv
runterlädt und in das input/-Verzeichnis speichert.
"""
import configparser 
import requests
import os.path
import pandas as pd

    
url = 'https://daten.stadt.sg.ch/explore/dataset/traktandierte-geschaefte-sitzungen-stadtparlament-stgallen/download/?format=csv&timezone=Europe/Zurich&lang=de&apikey=7245acf1923512959a7013430f7d0c28f66e3d0d079221585e15be62&use_labels_for_header=true&csv_separator=%3B'

def get_traktandierte_geschaefte():
    config = configparser.ConfigParser()
    config.read('./config.ini', encoding='utf-8')
    print(list(config.keys()))
    basedir = config['Verzeichnisse']['basedir']
    r = requests.get(url, allow_redirects=True)
    savepath = os.path.join(basedir,'input')
    fullfilename = os.path.join(savepath,'traktandierte-geschaefte-sitzungen-stadtparlament-stgallen.csv')
    with open(fullfilename, 'wb') as fh:
        fh.write(r.content)
    print(f'wrote to {fullfilename}.')
    inputcsv = pd.read_csv(fullfilename,sep=';')
    print(inputcsv.head())

if __name__=='__main__':
    print('current working dir:',os.getcwd())
    get_traktandierte_geschaefte()