__doc__="""
Skript, welches die Datei 
traktandierte-geschaefte-sitzungen-stadtparlament-stgallen.csv
runterlädt und in das input/-Verzeichnis speichert.
die Datei so bereitstellt, damit diese in den Klassifikator übergeben werden kann

"""
import configparser 
import requests
import os.path
import numpy as np
import ipdb
import pandas as pd
from glob import glob
import pickle
#from simp2 import predict  TODO! predict-Funktion importieren
    



def load_config(configfilename):
    config = configparser.ConfigParser()
    config.read(configfilename, encoding='utf-8')
    print(list(config.keys()))
    return config

def get_url(config):
    url = config['Links']['url']
    return url

def get_traktandierte_geschaefte(config):
    basedir = config['Verzeichnisse']['basedir']
    url = get_url(config)
    r = requests.get(url, allow_redirects=True)
    savepath = os.path.join(basedir,'input')
    fullfilename = os.path.join(savepath,'traktandierte-geschaefte-sitzungen-stadtparlament-stgallen.csv')
    with open(fullfilename, 'wb') as fh:
        fh.write(r.content)
    print(f'wrote to {fullfilename}.')
    inputcsv = pd.read_csv(fullfilename,sep=';')
    print(inputcsv.head())
    return fullfilename
  
def preprocess(df):
    """
    Vorverarbeitung des Dataframes.
    >>>prepocess(df)
    """
    pos = df['Aktenplan Ebene2'] == 'Stadtparlament (früher Gemeinderat, Grosser Gemeinderat)'
    df = df.loc[pos,:]
    df = df[['Traktandentitel']]
    df = df.rename(columns={'Traktandentitel':'X1'})
    df.index.name='Id'
    series = pd.Series(df.iloc[:,0])
    return series
      
def bereitstellen_csv_simple(fullfilename):
    df = pd.read_csv(fullfilename, sep=';')
    series = preprocess(df)
    return series
      
def read_pickle(classifier_pickle): 
    if not os.path.exists(classifier_pickle):
        raise FileNotFoundError(f'{classifier_pickle} not found')

    with open(classifier_pickle, 'rb') as fh:
        SVMStGallen = pickle.load(fh)
    return SVMStGallen

def get_classifier_from_pickle(basedir,pickle_fn):
    #picklepfad = os.path.join(basedir,'classifiers')
    #globpath=os.path.join(picklepfad,'*.pickle')
    #picklelist = glob(globpath)
    return read_pickle(pickle_fn)
    #if len(picklelist)==1:
        #return read_pickle(picklelist[0])
    #elif len(picklelist)==0:
        #print(f'keine Pickle-Datei gefunden:{globpath}')
        #return ''
    #elif len(picklelist)>1:
        #print(f'zu viele Pickle-Dateien! \n{picklelist}')
        #return ''

def predict_simp(series,classifier,k=3):
    phat_test = classifier.predict_proba(series)
    indices = np.argsort(phat_test,axis=1)[:,-k:]
    indices=indices[:,::-1]
    #recommendations = [str(ind)+','+' '.join(row)+'\n' for row,ind in 
    #recommendations = [str(ind)+';'+';'.join(row)+'\n' for row,ind in zip(indices.astype('str').tolist(),series.index)]
    # TODO: noch seeeehr unhübsch!!!
    recommendations = pd.DataFrame(indices,index=series.index)
    predictionind = pd.Series(np.argsort(phat_test,axis=1)[:,0],name='Vorhergesagte Klasse',index=series.index)
    df_klassenbeschreibung = pd.read_excel('input/Kategorienbeschreibung.xlsx')
    recommendations.columns = [f'Empfehlung {i}' for i in range(1,k+1)]
    classdict = df_klassenbeschreibung.set_index('KategorieNr').to_dict()['Kategorie']
    #d = classser['Kategorie'].to_dict()
    prediction = predictionind.map(classdict)
    recommendations = recommendations.applymap(lambda x:classdict[x])
    
    return prediction, recommendations


def main_simple_fun(config,keep_index=True):
    print('current working dir:',os.getcwd())    
    #url = 'https://daten.stadt.sg.ch/explore/dataset/traktandierte-geschaefte-sitzungen-stadtparlament-stgallen/download/?format=csv&timezone=Europe/Zurich&lang=de&apikey=7245acf1923512959a7013430f7d0c28f66e3d0d079221585e15be62&use_labels_for_header=true&csv_separator=%3B'
    url = get_url(config)
    fullfilename = get_traktandierte_geschaefte(config)
    series = bereitstellen_csv_simple(fullfilename)
    basedir = config['Verzeichnisse']['basedir']
    pickle_fn = os.path.join(basedir,'classifiers','SVMStGallen.pickle')
    classifier = get_classifier_from_pickle(basedir,pickle_fn)

    prediction, recommendations = predict_simp(series, classifier)
    print(prediction)
    if keep_index:
        prediction=pd.Series(prediction,index=series.index)
    else:
        series = series.values    
    return_df = pd.DataFrame({'X':series,'y':prediction})
    return_df = pd.concat([return_df,recommendations],axis = 1)
    return return_df

if __name__=='__main__':
    config = load_config('./config.ini')

    return_df = main_simple_fun(config)
    display
    

 

 