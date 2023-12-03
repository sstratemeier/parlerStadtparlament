__doc__="""
Skript, welches die Datei 
traktandierte-geschaefte-sitzungen-stadtparlament-stgallen.csv
runterlädt und in das input/-Verzeichnis speichert.
die Datei so bereitstellt, damit diese in den Klassifikator übergeben werden kann


"""
import sys
import spacy
import configparser
import os.path
import pandas as pd
from code.main_simple import main_simple_fun
from code.complex import main_complex_fun
from pathlib import Path
config = configparser.ConfigParser(interpolation=None)
configfile='config.ini' # TODO: mit ArgumentParser korrekten Wert aus optionalem Argument übernehmen
if not os.path.exists(configfile):
    raise FileNotFoundError('Es wurde keine Datei config.ini gefunden. Bitte config-sample.ini nach config.ini compieren und anpassen.')
config.read(configfile, encoding='utf-8')

#variant = 'simple' #TODO:to be read from configparser or config file!
variant=config['Einstellungen']['Variante']
if variant=='simple':
    df_predictions = main_simple_fun(config)
    df_predictions.to_excel('output/Vorhersagen.xlsx')
    basedir = config['Verzeichnisse']['basedir']
    savepath = os.path.join(basedir,'input')
    fullfilename = os.path.join(savepath,'traktandierte-geschaefte-sitzungen-stadtparlament-stgallen.csv')
    df_collect = pd.read_csv(fullfilename, sep=';')
    pos = df_collect['Aktenplan Ebene2'] == 'Stadtparlament (früher Gemeinderat, Grosser Gemeinderat)'
    df_collect = df_collect.loc[pos,:]
    df_collect['Vorhersage'] = df_predictions['y']
    df_collect['Empfehlung 1'] = df_predictions['Empfehlung 1']
    df_collect['Empfehlung 2'] = df_predictions['Empfehlung 2']
    df_collect['Empfehlung 3'] = df_predictions['Empfehlung 3']
    df_collect.to_excel('output/traktandierte-geschaefte-sitzungen-stadtparlament-stgallen_klassifiziert.xlsx')
    
elif variant=='ausführlich':
    nlp = spacy.load('de_core_news_md')
    config = configparser.ConfigParser()
    config.read("config.ini", encoding='utf-8')
    inputcsv = config['Verzeichnisse']['inputcsv']
    basedir = config['Verzeichnisse']['basedir']
    workdir = config['Verzeichnisse']['verarbeitungspfad']
    inputcsv = Path(inputcsv)
    basedir = Path(basedir)
    workdir = Path(workdir)
    startdate = pd.to_datetime(config['Verzeichnisse']['startdate'])
    ScratchPfad = config['Verzeichnisse']['verarbeitungspfad']
    pickle_fn = os.path.join(basedir,'classifiers','complexpickle.pickle')
    df_collect=main_complex_fun(inputcsv, basedir, workdir, startdate, pickle_fn)
    df_collect.to_excel('output/traktandierte-geschaefte-sitzungen-stadtparlament-stgallen_klassifiziert.xlsx')
    
else:
    raise ValueError('variant musss "simple" oder "ausführlich" sein!')