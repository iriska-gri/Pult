 
from config.settings import settings
import os
import zipfile
import getpass
import shutil
filePartName="Всеотчеты"
fname='2020.10'
result_date='123'
fileName = 'C:/Users/%s/Desktop/%s_%s.zip' %(getpass.getuser(),filePartName,result_date)
z = zipfile.ZipFile(fileName, 'a')  
folder = '{0}load/{1}'.format(settings['архивОКВЭД'],fname)
# shutil.make_archive(fileName, 'zip', folder)
for  files in os.listdir(folder):
    for f in os.listdir(os.path.join(folder,files)):
        print(f)
    # print(os.path.join(folder,files))
        if f.endswith('.xlsx'):
            z.write(os.path.join(folder,files,f), '{}\\{}'.format(files,f), compress_type = zipfile.ZIP_DEFLATED)
    
z.close()    
# shutil.rmtree('%sload/%s' %(settings['архивОКВЭД'],fname), ignore_errors=True)