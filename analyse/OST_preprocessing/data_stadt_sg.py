import argparse
import logging
import pdfplumber
import re
import pandas as pd
import os
import zipfile
import configparser 
from glob import glob
import tqdm
from tqdm import tqdm
from tqdm import tqdm
from pathlib import Path
from pdfminer.pdftypes import PDFException
from pdfminer.psparser import PSEOF
import requests
from zipfile import ZipFile
from zipfile import BadZipFile
import ipdb
import codecs
import numpy as np
tqdm.pandas()  # <- added this line
#tqdm_notebook.pandas()


def createdirectory(configfile,ScratchPfad=''):
    config = configparser.ConfigParser()
    config.read(configfile, encoding='utf-8')
    if not ScratchPfad:
        ScratchPfad = config['Verzeichnisse']['verarbeitungspfad']
    ScratchPfad = Path(ScratchPfad)
    Text_Pfad = ScratchPfad/'Text'
    PDF_Pfad = ScratchPfad/'PDF'
    ZIP_Pfad = ScratchPfad/'ZIP'

    for pfad in (Text_Pfad,PDF_Pfad,ZIP_Pfad):
        if not pfad.exists():
            os.makedirs(pfad,exist_ok=False)
        else:
            #raise FileExistsError(f'{pfad} existiert bereits')
            print(f'{pfad} existiert bereits')
    return Text_Pfad, PDF_Pfad, ZIP_Pfad


#Text_Pfad, PDF_Pfad, ZIP_Pfad=creatdirection('./config.ini')


def get_traktandierte_geschaefte(configfile):
    assert os.path.exists(configfile),f'File {configfile} does not exist.'
    config = configparser.ConfigParser(interpolation=None)
    config.read(configfile, encoding='utf-8')
    basedir = config['Verzeichnisse']['basedir']
    url = config['Links']['url']
    r = requests.get(url, allow_redirects=True)
    savepath = os.path.join(basedir,'input')
    fullfilename = os.path.join(savepath,'traktandierte-geschaefte-sitzungen-stadtparlament-stgallen.csv')
    with open(fullfilename, 'wb') as fh:
        fh.write(r.content)
    print(f'wrote to {fullfilename}.')
    inputcsv = pd.read_csv(fullfilename,sep=';')
    return inputcsv




def unzip(source_filename, dest_dir):
    with zipfile.ZipFile(source_filename) as zf:
        zf.extractall(dest_dir)


def cretatedir(dest):    
   #print('create',dest)
   os.makedirs(dest,exist_ok=True)
   return dest

# Create a ZipFile Object and load sample.zip in it
def extract(zipfn,dest,verbose=False):
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

def create_and_extract(zipfn,destdir,verbose=False):
   if verbose:
       print(f'creating dir {destdir}')
   dest = cretatedir(destdir)
   #print('dest',dest)
   #print('zipfn',zipfn)
   #if not os.path.exists(dest):
   extract(zipfn,dest)

def download_and_save(url,filename=None,verbose=False,zippath=None,pdfpath=None):
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

   #os.makedirs(scratchPath,exist_ok =True)
   

#    if not os.path.exists(zippath):
#        os.makedirs(zippath,exist_ok =True)
   if not os.path.exists(zipfn):
       # trying to be nice, see here:
       # https://stackoverflow.com/questions/23013220/max-retries-exceeded-with-url-in-requests
       from requests.adapters import HTTPAdapter
       from urllib3.util.retry import Retry

       session = requests.Session()
       retry = Retry(connect=3, backoff_factor=0.5)
       adapter = HTTPAdapter(max_retries=retry)
       session.mount('http://', adapter)
       session.mount('https://', adapter)

       r = session.get(url)
       #r = requests.get(url, allow_redirects=True)
       #assert  os.path.exists(zippath),'???'
       try:
           with open(zipfn, 'wb') as fh:
               fh.write(r.content)
       except PermissionError as err:
           print('--------',err)
           #ipdb.set_trace()
           return r,None
       if verbose:
           print(f'saved to {zipfn}',filename)
   else: 
       #print(zipfn,'already exists')
       r=None
   #print('scratchPath',scratchPath)
   extractpath = os.path.join(pdfpath,fr'{filename}')
   try:
       create_and_extract(zipfn,extractpath)
   except BadZipFile as err:
       print(zipfn)
       print(err)
       return None,zipfn
   return r,zipfn



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
#nur mal als Test kann später gelöscht werden:
#text = process_pdf(r"C:\Temp\Stadt_SG\downloads\extract\7099d3f0fbfb4a8695bd6419e5d3700b\Interpellation.pdf")
#text[:500]


def extract_text_from_pdf(pdf_fn,Text_Pfad):
    pdf_fn = Path(pdf_fn)
    Text_Pfad = Path(Text_Pfad)
    subdir = pdf_fn.parent.stem
    output_txt_fn = Text_Pfad/subdir/pdf_fn.with_suffix('.txt').name
    if output_txt_fn.exists():
        filesize = os.path.getsize(output_txt_fn)
    if not output_txt_fn.exists() or filesize < 100:
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
        except PSEOF as err:
            print(f'Die Datei {pdf_fn} ist offenbar korrupt')
            print(err)
            return 'pdfexception'
        except Exception as err:
            logging.error(f'Unbekannte Exception bei der Verarbeitung der Datei {pdf_fn}')
            raise
        os.makedirs(Text_Pfad/subdir,exist_ok=True)
        with open(output_txt_fn,'w',encoding='utf-8') as fh:
            fh.write(text)
        return 'success'
    else:
        #print(filesize,output_txt_fn)
        return 'file exists'        
    




#file = r'C:\Temp\Stadt_SG\downloads\extract\0ffcaafb3117404385b9fcf60739c613\Übersichtsplan, Kolumbanstrasse, Heimatstrasse bis Heiligkreuzstrasse; Verpflichtu - 24.11.2020 #1.pdf'
#file = r'C:\Temp\Stadt_SG\downloads\extract\1f9ecaa938b443bea854b8a32263e07b\LA Neudorf Planbeilage Bestand neu - 02.07.2021 #2.pdf'


def dump_to_csv(Text_Pfad):
    filelist = glob(os.path.join(Text_Pfad,'*\*.txt'))

    data = {}
    for file in filelist:
        with codecs.open(file,'r',encoding='utf-8') as fh:
            lines = fh.readlines()
        text = ''.join(lines)
        data[file]=text
    data_dict = {os.path.basename(k):v for k,v in data.items()}
    index = np.arange(len(data_dict))
    df = pd.DataFrame(data_dict,index=index)
    return df



def main(max_files=None):
    inputcsv = get_traktandierte_geschaefte('./config.ini')
    urls = inputcsv['Download Traktandumsdokumente']
    inputcsv['basenames']=urls.dropna().apply(lambda url: os.path.splitext(os.path.basename(url))[0])# kann gelöscht werden


    Text_Pfad, PDF_Pfad, ZIP_Pfad = createdirectory('./config.ini')
#
    url_ser = inputcsv['Download Traktandumsdokumente']
    #ser1 = url_ser.dropna().map(lambda url:Path(url).name)
    zip_already_exists_LA = url_ser.dropna().map(lambda url:Path(url).name).map(lambda zipfile:os.path.exists(os.path.join(ZIP_Pfad,zipfile)))

    inputcsv_zip = inputcsv.loc[zip_already_exists_LA[~zip_already_exists_LA].index]

    logging.info(f'Downloading zip files to {ZIP_Pfad}')
    if max_files is not None:
        inputcsv_zip.loc[:,'Download Traktandumsdokumente'].dropna().iloc[:max_files].progress_apply(lambda s: download_and_save(s,zippath=ZIP_Pfad,pdfpath=PDF_Pfad))
    else:
        inputcsv_zip.loc[:,'Download Traktandumsdokumente'].dropna().progress_apply(lambda s: download_and_save(s,zippath=ZIP_Pfad,pdfpath=PDF_Pfad))
    print(f'extracting to {PDF_Pfad} and then to {Text_Pfad}...\n')

    #Bestimme PDF-Dateien, welche nicht existieren, wobei die zugehörigen Zip-Dateien existieren. Für diese ist die Extraktion vorzunehmen. 
    pdf_already_exists_LA = url_ser.dropna().map(lambda url:Path(url).with_suffix('').name)
    pdf_already_exists_LA = pdf_already_exists_LA .map(lambda G_GUID:os.path.exists(os.path.join(PDF_Pfad,G_GUID)))

    zip_but_not_pdf_LA = zip_already_exists_LA & (~pdf_already_exists_LA)
    zip_but_not_pdf_LA = zip_but_not_pdf_LA[zip_but_not_pdf_LA] 
    zips_to_extract = urls.loc[zip_but_not_pdf_LA.index].map(lambda url:Path(url).with_suffix('').name)

    # Extraktion der Zip-Dateien
    logging.info(f'Extraction zip files to {PDF_Pfad}')
    for filename in zips_to_extract:
        zipfn = (ZIP_Pfad/filename).with_suffix('.zip')
        extractpath = PDF_Pfad/fr'{filename}'
        if zipfn.exists():
           try:
               create_and_extract(zipfn,extractpath)
           except BadZipFile as err:
               print(zipfn)
               print(err)

    #Bestimme die Geschäfts_GUID(-Verzeichnisse), für welche ein Verzeichnis für extrahierte PDF-Dateien existiert, aber noch kein Verzeichnis für die (daraus extrahierten) Textdatei(en)
    text_already_exists_LA = url_ser.dropna().map(lambda url:Path(url).with_suffix('').name)
    text_already_exists_LA = text_already_exists_LA.map(lambda G_GUID:os.path.exists(os.path.join(Text_Pfad,G_GUID)))
    inputcsv_text = inputcsv.loc[text_already_exists_LA[~text_already_exists_LA].index]

    # Textextraktion aus PDF-Dateien
    logging.info(f'Extracting Text from PDF files to {Text_Pfad}')
    logging.info(f'{inputcsv_text.shape[0]} GUIDs müssen verarbeitet werden.')
    pbar = tqdm(inputcsv_text.Geschaeft_GUID.dropna())
    for pdf_fn in pbar:
        pbar.set_description(f"Textextraction from PDFs {pdf_fn}")
        curr_pdf_path = Path(PDF_Pfad)/pdf_fn
        if (Text_Pfad/pdf_fn).exists():
            continue
        pdffiles = curr_pdf_path.glob('*.pdf')
        for curr_pdf in curr_pdf_path.glob('*.pdf'):
            try:
                returnmsg = extract_text_from_pdf(curr_pdf,Text_Pfad=Text_Pfad)
            except FileNotFoundError as err:
                print('FEHLER:',err,f'überspringe Datei {pdf_fn}')
                continue
    #ipdb.set_trace()
    logging.info(f'Done writing to {Text_Pfad}.')

if __name__=='__main__':
    main(max_files=None)
