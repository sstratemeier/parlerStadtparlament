import pandas as pd
import swifter
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
import spacy
import pickle
import configparser
import re
import os
import ipdb
import zipfile
import pdfplumber
from glob import glob
import tqdm
from tqdm import tqdm
from tqdm.notebook import tqdm_notebook
from pdfminer.pdftypes import PDFException
import requests
from zipfile import ZipFile
from zipfile import BadZipFile
import ipdb
import codecs
from pathlib import Path



def unzip(source_filename, dest_dir):
    with zipfile.ZipFile(source_filename) as zf:
        zf.extractall(dest_dir)

def load_pickle(pickle_fn):
    with open(r".\classifiers\complexpickle.pickle", 'rb') as f:
        loaded_obj = pickle.load(f)
    vct1 = loaded_obj["vct1"]
    vct2 = loaded_obj["vct2"]
    clf1 = loaded_obj["clf1"]
    clf2 = loaded_obj["clf2"]
    clf3 = loaded_obj["clf3"]
    print(loaded_obj)
    return vct1,vct2,clf1,clf2,clf3

def cretatedir(dest):    
    os.makedirs(dest,exist_ok=True)
    return dest

def extract(zipfn,dest,verbose=False):
    try: 
        with ZipFile(zipfn, 'r') as zipfile:
           # Extract all the contents of zip file in current directory
            try:
                zipfile.extractall(path=dest)
            except OSError as err:
                print(err)
                print(f'Extraction failed for {zipfn},{dest}')
                print(zipfile.namelist())
                #ipdb.set_trace()
                """dest = dest.replace('\r\n','')
                destfiles = [s.replace('\n','').replace('\r','').replace(')','') for s in zipfile.namelist()]
                for filename,dest in zip(zipfile.namelist(),destfiles):
                    filenamenew = filename.replace('\n','').replace('\r','').replace(')','')
                    zipfile.extract(filename,path=os.path.join(dest,filenamenew))
                    print(f'extracted {filename} to {dest}')
                """
            if verbose:
                print(f'extracted to {dest}')
    except BadZipFile as err:
        print(err)
        ipdb.set_trace

def create_and_extract(zipfn,destdir,verbose=False):
    if verbose:
        print(f'creating dir {destdir}')
    dest = cretatedir(destdir)
    #print('dest',dest)
    #print('zipfn',zipfn)
    #if not os.path.exists(dest):
    extract(zipfn,dest)
    

def download_and_save(url,zippath,pdfpath,filename=None,verbose=False):
    """
    >>>download_and_save(url,zippath=ZIP_Pfad,pdfpath=PDF_Pfad)
    (<Response [200]>,
 'C:\\Temp\\Stadt_SG2\\ZIP\\00e39bd219f34918a9cbc202682fd945.zip')
    """
    if filename is None:
        filename = os.path.splitext(os.path.basename(url))[0]
   # zippath = os.path.join(scratchPath,f'zip')
    zipfn=os.path.join(zippath,f'{filename}.zip')
    #print(scratchPath,filename,zipfn)
    #ipdb.set_trace()
    #os.makedirs(scratchPath,exist_ok =True)
    

#    if not os.path.exists(zippath):
#        os.makedirs(zippath,exist_ok =True)
    if not os.path.exists(zipfn):
        r = requests.get(url, allow_redirects=True)
        assert  os.path.exists(zippath),'???'
        try:
            with open(zipfn, 'wb') as fh:
                fh.write(r.content)
        except PermissionError as err:
            print('--------',err)
            ipdb.set_trace()
            return r,None
        if verbose:
            print(f'saved to {zipfn}',filename)
    else: 
        #print(zipfn,'already exists')
        r=None
    #print('scratchPath',scratchPath)
    extractpath = os.path.join(pdfpath,fr'{filename}')
    create_and_extract(zipfn,extractpath)
    return r,zipfn


def extracttext(s):
    print(s)
    if s=="":
        return ""
    else:   
        files = glob(os.path.join(s,'*'))
        text={}
        i=0
        x=""
        for file in files:
                    with codecs.open(file, "r", "utf-8") as fh:
                        lines = fh.readlines()
                        text[i] = ' '.join(lines).replace('- ','')
                        text[i] = re.sub(r"\d+([']\d+)*",'<NUMBER>',text[i])
                        if len(text[i]) > 100000:
                            text[i]=text[i][:100000]
                    i = i+1
        for n in range(0,i):
            x = x+text[n]
        return x

def extractspacysvector(s):
    nlp = spacy.load('de_core_news_md')
    x = extracttext(s)
    doc = nlp(x)
    a= doc.vector
    return a

def spacylemma(s):
    nlp = spacy.load('de_core_news_md')
    doc = nlp(s)
    a = ""
    for token in doc:
        a = a+ token.lemma_+" " 
    return a

#dftest = pd.read_csv(os.path.join(inputcsv))

def construct_dfpd(y_hat1, y_hat2, y_hat3, dftest, basedir):
    a= pd.DataFrame(y_hat1) #auf Titeln mit SVM
    b= pd.DataFrame(y_hat2) #auf allem mit SPACY
    c= pd.DataFrame(y_hat3) #auf allem mit tfidf und SVM
    dfpd = (5*a+3*b+8*c)/16
    dfpd["score1"] = dfpd.max(axis=1)
    dfsub=dfpd
    dfpd=dfpd.drop("score1",axis=1)
    dfpd["best"] = dfpd.idxmax(axis=1)
    #dfpd["score1"] = dfpd.max(axis=1) #check this
    for i in range (0,17):
        dfpd.loc[(dfpd.best == i), i] = 0
    dfsub["best"]=dfpd["best"]
    dfpd=dfpd.drop("best",axis=1)
    dfpd["score2"] = dfpd.max(axis=1)
    dfsub["score2"]=dfpd["score2"]
    dfpd=dfpd.drop("score2",axis=1)
    dfpd["second"] = dfpd.idxmax(axis=1)
    #dfpd["score2"] = dfpd.max(axis=1) #check this
    for i in range (0,17):
        dfpd.loc[(dfpd.second == i), i] = 0
    dfsub["secondbest"]=dfpd["second"]
    dfpd=dfpd.drop("second",axis=1)
    dfpd["score3"] = dfpd.max(axis=1)
    dfsub["score3"]=dfpd["score3"]
    dfpd=dfpd.drop("score3",axis=1)
    dfpd["third"] = dfpd.idxmax(axis=1)
    dfsub["thirdbest"]=dfpd["third"]
    dfsubs=dfsub[["best", "secondbest", "thirdbest", "score1", "score2", "score3"]]
    dfcatlist = pd.read_excel(os.path.join(basedir, "processing/Kategorienbeschreibung.xlsx"))
    dfcatlist = dfcatlist.set_index('KategorieNr').to_dict()
    dfsubs.loc[:,"best"]=dfsubs['best'].map(lambda key:dfcatlist['Kategorie'][key])
    dfsubs.loc[:,"secondbest"]=dfsubs["secondbest"].map(lambda key:dfcatlist['Kategorie'][key])
    dfsubs.loc[:,"thirdbest"]=dfsubs.thirdbest.map(lambda key:dfcatlist['Kategorie'][key])
    return dfsubs

def predict_comp(dftest,pickle_fn,basedir):
    nlp = spacy.load('de_core_news_md')
    with open(pickle_fn,'rb') as fh:
        object_file = pickle.load(fh)
    
    vct1 = object_file.get("vct1")
    vct2 = object_file.get("vct2")
    clf1 = object_file.get("clf1")
    clf2 = object_file.get("clf2")
    clf3 = object_file.get("clf3")
    #print(vct1) #you can't print that- raises an error
	# vct1,vct2,clf1,clf2,clf3 = load_pickle(os.path.join(pickle_fn))
    print('performing lemmatization...')
    dftest['X2']=dftest.Traktandentitel.apply(spacylemma)
    print('performing vectorization...')
    XTest1 = vct2.transform(dftest.X2)
    XTest1=XTest1.toarray()
    print('generating predictions...')
    y_hat1 = clf1.predict_proba(XTest1)
    XTest2 = dftest.path.apply(extractspacysvector)
    XTest2 = np.array(XTest2.values.tolist())
    Test = dftest.path.apply(extracttext)
    XTest3 = vct1.transform(Test)         
    y_hat2 = clf2.predict_proba(XTest2) 
    y_hat3 = clf3.predict_proba(XTest3)
    dfpd=construct_dfpd(y_hat1, y_hat2, y_hat3, dftest, basedir) 
    del dftest['X2']
    dftest=dftest.copy()
    for col in dfpd.columns:
        dftest.loc[:,col]=dfpd[col].values
    return dftest

def preprocess_Text(s):
    s = re.sub('\n *',' ',s)
    s = re.sub('  +',' ',s)
    return s
    
def process_pdf(pdffile):
    with pdfplumber.open(pdffile) as pdf:
        pagelist = [page.extract_text() for page in pdf.pages]
        Text = ' '.join(pagelist)
        s = preprocess_Text(Text)
    return s

def process_file(pdf_fn,Text_Pfad):
    subdir = os.path.split(os.path.split(pdf_fn)[0])[1]
    output_txt_fn = pdf_fn.replace('.pdf','.txt')
    output_txt_fn =  os.path.join(Text_Pfad,subdir,os.path.basename(output_txt_fn))
    if os.path.exists(output_txt_fn):
        filesize = os.path.getsize(output_txt_fn)
    if not os.path.exists(output_txt_fn) or filesize < 100 or filesize >1000000:
        try:
            text = process_pdf(pdf_fn)
        except ValueError as err:
            print(f"Error {err}")
            print(f"Datei war {pdf_fn}")
            print(err,'skipping')
            return 'valueerror'
        except PDFException as err:
            print(err)
            print(f'Exception at {pdf_fn}')
            return 'pdfexception'
        os.makedirs(os.path.join(Text_Pfad,subdir),exist_ok=True)
        #print(f'{ipdf} of {L}: {output_txt_fn}')
        os.path.split(output_txt_fn)
        with open(output_txt_fn,'w',encoding='utf-8') as fh:
            fh.write(text)
        return 'success'
    else:
        #print(filesize,output_txt_fn)
        return 'file exists'     
    
    

def main_complex_fun(inputcsv, basedir, workdir, startdate, pickle_fn,do_download=True,do_process=True,do_parallel=True):

    if not os.path.exists(basedir):
        raise FileNotFoundError(f'Das Verzeichnis {basedir} existiert nicht. Bitte erstellen Sie es oder ändern Sie den Eintrag von "basedir" in der Datei config.ini.' )
    nlp = spacy.load('de_core_news_md')
    ScratchPfad = workdir
    Text_Pfad = os.path.join(ScratchPfad,'Text')
    PDF_Pfad = os.path.join(ScratchPfad,'PDF')  
    ZIP_Pfad = os.path.join(ScratchPfad,'ZIP')
    
    for pfad in (Text_Pfad,PDF_Pfad,ZIP_Pfad):
        if not os.path.exists(pfad):
            os.makedirs(pfad,exist_ok=False)
        else:
            #raise FileExistsError(f'{pfad} existiert bereits')
            print(f'{pfad} existiert bereits')
    if not os.path.exists(inputcsv):
        raise FileNotFoundError(f'Datei {inputcsv} wurde nicht gefunden. Ev. muss in der config.ini-Datei der Eintrag "inputcsv" unter "Einstellungen" angepasst werden.')
    ipdb.set_trace()
    df1 = pd.read_csv(os.path.join(inputcsv),sep=';')
    df1["index"]=df1.index
    filelist = glob(os.path.join(workdir,r'extracts\*'))
    df1['Dokumentendatum'] = pd.to_datetime(df1['Dokumentendatum'])
    dftest = df1[(df1['Dokumentendatum'] > startdate)].copy()
    del df1
    if dftest.shape[0]==0:
        print(dftest.head())
        raise ValueError(f'Keine Werte mit Dokumentendatum später als {startdate} gefunden.')
    urls = dftest['Download Traktandumsdokumente']
    if do_download:
        dftest['Download Traktandumsdokumente'].dropna().swifter.apply(lambda s: download_and_save(s,zippath=ZIP_Pfad,pdfpath=PDF_Pfad))

    l = glob(os.path.join(PDF_Pfad,r'*\*.pdf'))


    if do_process:
        if do_parallel:
            l = pd.Series(l,name='pdfs')
            l.swifter.apply(lambda pdf_fn:process_file(pdf_fn,Text_Pfad))
        else:
            t = tqdm(l)
            for pdf_fn in t:
                    t.set_postfix(file=f'{pdf_fn:.<100}')
                    try:
                        process_file(pdf_fn, Text_Pfad)
                    except:
                        continue 
    print(f'Done. Wrote to {Text_Pfad}')

    ifound=0
    inotfound=0
    for index,fn in dftest['Geschaeft_GUID'].dropna().items():
        g_GUID = fn
        found_any=False
        path=os.path.join(Text_Pfad,g_GUID)
        if os.path.exists(path):
            found_any=True
        if found_any:
            ifound+=1
            dftest.loc[index,'path']=path
        else:
            inotfound+=1
            dftest.loc[index,'path']= '%snew_direct_test_%s' % (Text_Pfad,str(inotfound))

    print(ifound,'found,',inotfound,'not found')



    # Leere füllen

    newdf = dftest[(dftest.path.isna())]
    for Id in newdf.index:
        dftest.loc[Id,'path'] = '{0}\\Text\\ReplaceNAN{1}'.format(workdir,Id)

    for irow,  row in dftest.iterrows():
        os.makedirs(row.path, exist_ok=True);
        with open("%s/title220407" % row.path, 'w', encoding='utf8') as output_file:
            output_file.write(row.Traktandentitel)
    
    dftest1 = predict_comp(dftest, pickle_fn,basedir)
    csvfile = os.path.join(basedir,r"output\predtictedcsv.csv")
    dftest1.to_csv(path_or_buf=csvfile)
    print(f'wrote to {csvfile}.')
    return dftest1

    
if __name__ == "__main__":
    nlp = spacy.load('de_core_news_md')
    config = configparser.ConfigParser()
    config.read("../config.ini", encoding='utf-8')
    inputcsv = config['Verzeichnisse']['inputcsv']
    basedir = config['Verzeichnisse']['basedir']
    workdir = config['Verzeichnisse']['verarbeitungspfad']
    startdate = config['Verzeichnisse']['startdate']
    ScratchPfad = config['Verzeichnisse']['verarbeitungspfad']
    pickle_fn = os.path.join(basedir,'classifiers','complexpickle.pickle')
    if not os.path.exists(pickle_fn):
        raise FileNotFoundError(f"Die Datei {pickle_fn} ist am angegeben Ort nicht verfügbar")
    main_complex_fun(inputcsv, basedir, workdir, startdate, pickle_fn)
