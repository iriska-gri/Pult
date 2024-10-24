from io import BytesIO
import pandas as pd
import json
import requests
import base64
from config.orm import Orm
from config.settings import settings
import getpass
# from .create_dict import Diction
from datetime import datetime, timedelta
import time
import random
from config.settings import datar
# from config.create_excel import createwb
import os
import zipfile
from os import path, remove, listdir
from pandas.io.json import json_normalize
#from lxml import etree
import openpyxl
import shutil
import subprocess
import urllib

from win32com.client import Dispatch, DispatchEx
import pythoncom
def delete_files(dir_name: str):
    ''' Удаляет все файлы из выбранной папки '''

    filelist = [ f for f in listdir(dir_name)]
    for f in filelist:
        remove(path.join(dir_name, f))



def upload_datakkt(start=''):
    
    print (start)
    orm_ = Orm()
    orm_.inserttimekey('prices.lasttry','try', datetime.now())
    orm_.commit_to()
    for key, value in datar.items():
        
        result_date = datetime.strptime(start, "%Y-%m-%d")
        result_date_convert = result_date.strftime("%Y-%m-%dT%H:%M:%S.")
        def isNaN(num):
            return num != num
        

        try:

            f = requests.get('https://cluster-analysis.nalog.ru/webproxy/api/'+key+'?dateTime=' + result_date_convert + str(int(random.random()*1000)) + 'Z&apikey=d808c003f1d69c5fa97713b2a5e1b591')
            encoded = json.loads(f.text)
            data = base64.b64decode(encoded['content'])
            toread = BytesIO()
            toread.write(data)  # pass your 'decrypted' string as the argument here
            toread.seek(0)  # reset the pointer
            timer_work = time.monotonic()
        except Exception:
            print("провал загрузки {}".format(key))
            continue
        for val in range(len(value)):
        
            df = pd.read_excel(toread,sheet_name=val,header=None) #номер листа с 0
                
            if key == 'consumerbasketreport/summary/download/':
                del df[1]
                df.insert(loc=0, column='datelikedale', value=result_date.strftime("%Y-%m-%d"))
            elif key =='OkvedReport/new/okved/download/base64': 
                df.insert(loc=0, column='datelikedale', value=result_date.strftime("%Y-%m-%d")) 
                df=df.fillna(0)
                df=df.replace("-",0)
                df2=df.drop(df.columns[2:88], axis='columns', inplace=False) 
                df = df.drop(df.columns[88:174], axis='columns', inplace=False) 
            else:
                df[0] = result_date.strftime("%Y-%m-%d")
                del df[2]
            flag = True
                    
            for i in range(df.shape[0]-1):
            
                    j = 0 if isNaN(df.iloc[i,df.shape[1]-1]) else i
                    
                    if  j != 0:
                        if key in ['consumerbasketreport/summary/download/','DrugReport/download/base64','revenueByRegion/revenue_and_kkt/download/base64']:
                            skip=i+1
                        else:
                            skip=i+2
                        if key in ['ExtendedConsumerBasket/avg_price_and_consumption/download/base64','DrugReport/download/base64']:
                            df=df.fillna(0)
                        if key =='OkvedReport/new/okved/download/base64':  
                            skip=i+4 
                            arr2 =str(tuple(df2.loc[skip]))
                            
                            
                        if flag:
                            if sum(tuple(df.loc[skip])[2:]) != 0:
                                flag = False
                            
                        arr =str(tuple(df.loc[skip]))
                        if tuple(df.loc[skip])[1]=='Итого':
                            continue                      
                        orm_.insert_tokkt(arr, value[val])
                        if key == 'OkvedReport/new/okved/download/base64':
                            orm_.insert_tokkt(arr2, "%sMSP" %value[val][:-2] )   

                        if (key not in ['consumerbasketreport/summary/download/','OkvedReport/new/okved/download/base64']) and (((df.iloc[skip][1])==99) or (isNaN(df.iloc[skip][1]) == True) or ((df.iloc[skip][1])==92 and ((df.iloc[skip+1][1])!=99))):
                            break
                        if key == 'OkvedReport/new/okved/download/base64'and (df.iloc[skip][0])==0:
                            break

            if not flag:
                print('Залил %s' % key)
                if key =='OkvedReport/new/okved/download/base64': 
                    orm_.commit_to()
            else:
                orm_.rollback()
                print('Не залил %s' %key) 


        delta = time.monotonic() - timer_work
        if delta <= 0.3:
            time.sleep(0.3 - delta)
            print(delta)
        
    print('Заливка прошла успешно')
    print('---------------------------')
    orm_.connclose()

  
    

def download_all_origins(clicked,start,end_date=''):
    folderlist = ('1 выручка','1.1 действующие', '2 цены', '3 лекарства','4 ТЭК','5 расширенный','Моногорода','Сахар_масло','Сахар_масло_ИНН','7 ОКВЭД','7.1 ОКВЭД сокр')
    # ,'7.2 ОКВЭД сокр'
    pythoncom.CoInitialize()
    
    dataro = ('revenueByRegion/new/revenue_and_reg_data/download/base64','revenueByRegion/new/revenue_and_kkt/download/base64',
    'consumerbasketreport/summary/download','DrugReport/download/base64','tecreport/avg_price_and_consumption/download/base64',
    'ExtendedConsumerBasket/avg_price_and_consumption/download/base64','MonocityReport/new/monocity/download/base64',
    'OilSugarReport/download/base64', 'OilSugarReport/by_inn/download/base64',
    'OkvedReport/new/okved/download/base64')
    scripts = ('ReportOKVED71.js','ReportOKVED72.js')
    # 
    dstart=start
    delete_files('{}load'.format(settings['архивОКВЭД']))
    if clicked!='kkttozip':
        end_date=dstart
    while dstart<=end_date:
        # if clicked=='kkttozip':
            
        start=dstart.strftime("%Y-%m-%d")
                    
    # orm_ = Orm()
        result_date = datetime.strptime(start, "%Y-%m-%d")  
        fname = result_date.strftime("%Y.%m")
        result_date_convert = result_date.strftime("%Y-%m-%dT%H:%M:%S.")
        for it in range(0,len(folderlist)):
            
            if it==0:
                
                
                os.makedirs('{}load/{}'.format(settings['архивОКВЭД'],fname), exist_ok=True) 
            if it<=9:    
                
                    
                f = requests.get('https://cluster-analysis.nalog.ru/webproxy/api/{0}?dateTime={1}{2}Z&apikey=d808c003f1d69c5fa97713b2a5e1b591'.format(dataro[it],result_date_convert,str(int(random.random()*1000))))
                # ---------------------------------------
                df = pd.json_normalize(f.json())
                encoded = json.loads(f.text)
                data = base64.b64decode(encoded['content'])
                filenames = encoded['fileName']
                print(filenames)
                xlsx = BytesIO(data)
                wb=openpyxl.load_workbook(xlsx)
                if clicked=='kkttozip':
                    os.makedirs('{}load/{}/{}/'.format(settings['архивОКВЭД'],fname,folderlist[it]), exist_ok=True)     
                    wb.save('{}load/{}/{}/{}'.format(settings['архивОКВЭД'],fname,folderlist[it],filenames ))
                else:
                    wb.save('{}load/{}/{}'.format(settings['архивОКВЭД'],fname,filenames ))
                if it==9 and clicked!='kkttozip':
                    os.makedirs('{}load/{}/{}'.format(settings['архивОКВЭД'],fname,folderlist[it]+fname), exist_ok=True) 
                    wb.save('{0}load/{1}/{2}{1}/{3}'.format(settings['архивОКВЭД'],fname, folderlist[it],filenames))
                    
                wb.close()
                
            elif it>9 and it<=10 and clicked=='kktnalog': 
                
                os.makedirs('{0}load/{2}/{1}{2}'.format(settings['архивОКВЭД'],folderlist[it],fname), exist_ok=True)
                
                filenames = os.listdir('{0}load/{2}/{1}{2}'.format(settings['архивОКВЭД'],folderlist[9],fname))
               
                shutil.copyfile('{0}load/{2}/{1}{2}/{3}'.format(settings['архивОКВЭД'], folderlist[9], fname,filenames[0],folderlist[it] ),'{0}load/{2}/{4}{2}/{3}'.format(settings['архивОКВЭД'], folderlist[9], fname,filenames[0],folderlist[it] ))
                
                shutil.copyfile('{0}script/{1}'.format(settings['архивОКВЭД'],scripts[0]), '{0}load/{2}/{3}{2}/{1}'.format(settings['архивОКВЭД'],scripts[0],fname,folderlist[it]))
                
                subprocess.run([ settings['архивОКВЭД'][:2],'&', 'cd',settings['архивОКВЭД']+'load/'+ fname+'/' + folderlist[it] + fname,'&', scripts[0]], shell=True)           
                
                os.remove('{0}load/{1}/{2}{1}/{3}'.format(settings['архивОКВЭД'],fname,folderlist[it],filenames[0]))
                os.remove('{0}load/{1}/{2}{1}/{3}'.format(settings['архивОКВЭД'],fname,folderlist[it],scripts[0] ))
                for files in (os.listdir('{0}load/{1}/{2}{1}/'.format(settings['архивОКВЭД'],fname,folderlist[it]))):
                    shutil.copyfile('{0}load/{1}/{2}{1}/{3}'.format(settings['архивОКВЭД'],fname,folderlist[it], files), '{0}load/{1}/{3}'.format(settings['архивОКВЭД'],fname,folderlist[it], files))
            if it in[0,1,6]:
                if it == 0:
                    Excel = DispatchEx("Excel.Application") # start excel
                    Excel.Visible = True # Visualization
                    Excel.DisplayAlerts = False # Whether to display warnings
                if clicked=="kkttozip":
                    fame='{0}load/{1}/{2}/{3}'.format(settings['архивОКВЭД'],fname, folderlist[it],filenames)
                else:
                    fame='{}load/{}/{}'.format(settings['архивОКВЭД'],fname,filenames )
                Wb = Excel.Workbooks.Open(fame) # Open excel
                Wb.Close(SaveChanges=1)
                if it ==6:
                    Excel.Quit()

            fileName = it

            if it==len(folderlist)-1 and dstart==end_date: 
                print('Создание архива')
                if clicked=='kkttozip':
                     filePartName="Всеотчеты"
                else:    
                    filePartName="ClusterDailyReport"
                fileName = 'C:/Users/%s/Desktop/%s_%s.zip' %(getpass.getuser(),filePartName,result_date.strftime("%Y_%m_%d"))
                
                z = zipfile.ZipFile(fileName, 'w')  
                folder = '{0}load/{1}'.format(settings['архивОКВЭД'],fname)
                if clicked=='kkttozip':
                    for  files in os.listdir(folder):
                        for f in os.listdir(os.path.join(folder,files)):
                            if f.endswith('.xlsx'):
                                z.write(os.path.join(folder,files,f), '{}\\{}'.format(files,f), compress_type = zipfile.ZIP_DEFLATED)
                elif clicked!='kkttozip':
                    for  files in os.listdir(folder):
                        if files.endswith('.xlsx'):
                            z.write(os.path.join(folder,files), os.path.relpath(files, ''), compress_type = zipfile.ZIP_DEFLATED)
                z.close()    
                
        
        dstart+=timedelta(days=1)
    shutil.rmtree('%sload/%s' %(settings['архивОКВЭД'],fname), ignore_errors=True)
    pythoncom.CoUninitialize()
    print('Готовенько')






