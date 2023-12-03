__doc__="""
Ein GUI zum Edititeren der Konfigurationsdatei. Eine PySimpleGUI-Oberfläche, 
mit der die Konfigurationsdatei bearbeitet werden kann.
Es wird config.ini eingelesen (die Konfig-Datei kann auch ausgewählt werden), und eine neue Datei config_edited.ini geschrieben.
Aktuell kann das Ausgabeverzeichnis, die Eingabe-CSV-Datei und die Konfig-Datei 
verändert werden.
"""
import configparser
import os
import PySimpleGUI as sg


def TextLabel(text):
    return sg.Text(text + ':', justification='r', size=(15, 1))
def run_window(config):
    sg.theme('DarkAmber')  # Add a touch of color
    # All the stuff inside your window.
    layout = [[sg.Text('Konfiguration')],
              # [sg.Text('Enter something on Row 2'), sg.InputText()],
              [TextLabel('Outputverzeichnis'), sg.Input(default_text=config['Verzeichnisse']['verarbeitungspfad'],key='-Outputverzeichnis-'),
               sg.FolderBrowse(target='-Outputverzeichnis-')],
              [sg.Text('CSV Datei', justification='right'), sg.InputText(size=(65, 1), key='csvdatei',default_text=config['Verzeichnisse']['verarbeitungspfad']),
               sg.FileBrowse(
                   size=(10, 1), file_types=(("Alle Dateien", "*"), ("CSV-Datei", "*.csv"), ("Excel-Datei", "*.xlsx"))
               )],
              [sg.Text('Config-Datei', justification='right'), sg.InputText(size=(65, 1), key='Config-Datei'),
               sg.FileBrowse(
                   size=(10, 1), file_types=(("Config-Datei", "*.ini"), ("Alle Dateien", "*"))
               )],
              [sg.Button('Ok'), sg.Button('Cancel'), sg.Sizegrip()]
              ]

    # Create the Window
    window = sg.Window('Window Title', layout, resizable=False)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        print('event', event)
        print('values', values)
        if event == 'Ok':
            Outputverzeichnis = values['-Outputverzeichnis-']
            CSVDatei = values['csvdatei']
            print('neues Outputverzeichnis', Outputverzeichnis)
            print('neue CSV-Datei', CSVDatei)
            break
        if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
            return values
        # print('You entered ', values[0])

    window.close()
    return values

if __name__=='__main__':
    config = configparser.ConfigParser()
    config.read('config.ini')
    values = run_window(config)
    Outputverzeichnis = values['-Outputverzeichnis-']
    config['Verzeichnisse']['verarbeitungspfad']=Outputverzeichnis

    CSVDatei = values['csvdatei']
    config['Verzeichnisse']['verarbeitungspfad'] = CSVDatei

    with open('edited_config.ini', 'w') as configfile:
        config.write(configfile)
    print('returnvals', values)
    print('neues Outputverzeichnis', Outputverzeichnis)
    print('neue CSV-Datei', CSVDatei)
    print('Es wurde in die Datei',os.path.join(os.getcwd(),'edited_config.ini'),'geschrieben.')
