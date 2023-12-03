import configparser
import os
import pandas as pd
import pytest

@pytest.fixture
def config():
    config = configparser.ConfigParser(interpolation=None)
    configfile='config.ini'
    config.read(configfile, encoding='utf-8')
    return config

@pytest.fixture
def inputcsv_fn(config):
    inputcsv = config['Verzeichnisse']['inputcsv']
    return inputcsv

@pytest.fixture
def inputcsv(inputcsv_fn):
    df=pd.read_csv(inputcsv_fn,sep=';')
    return df

def test_config_file_contents(config):
    assert 'Variante' in config['Einstellungen'], "Variante muss im Abschnitt 'Einstellungen' der Konfig-Datei angegeben werden: simple oder ausführlich"
    assert 'startdate' in config['Verzeichnisse'], "Startdatum muss im Abschnitt 'Verzeichnisse' angegeben werden"
    assert 'url' in config['Links'], "URL muss im Abschnitt 'Links' angegeben sein"
def test_csv_location(inputcsv_fn):
    assert os.path.exists(inputcsv_fn), "Kein File unter Path"
    assert inputcsv_fn.endswith(".csv"), "Filename hat falschen Suffix"

def check_if_col_exists(col, df):
    assert col in df, f"Spaltenname '{col}' nicht gefunden"

def test_csv_file_size(inputcsv_fn):
    assert os.path.getsize(inputcsv_fn) > 100000, "Inputfile ist unverhältnismässig klein"
    assert os.path.getsize(inputcsv_fn) < 100000000, "Inputfile ist unverhältnismässig gross"

def test_csv_file(inputcsv):
    df=inputcsv
    check_if_col_exists("Traktandentitel", df)
    check_if_col_exists("Dokumentendatum", df)
    check_if_col_exists("Geschaeft_GUID", df)
    assert df.shape[0]>100, "Inputfile hat unverhältnismässig wenig Zeilen"
    assert df.shape[0]<50000, "Inputfile hat unverhältnismässig viele Zeilen"
    assert df.shape[1]>10, "Inputfile hat unverhältnismässig wenig Spalten"
    assert df.shape[1]<200, "Inputfile hat unverhältnismässig viele Spalten"
    
   
    
    
   
