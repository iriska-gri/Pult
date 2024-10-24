import pickle
from pathlib import Path
from config.settings import settings
import datetime
import getpass

# getpass.getuser() - получить имя пользователя
class Properties:
    # словарь персональных настроек, свой для каждого компа
    def exists(self,path):
        try:
            Path(path).exists()
        except OSError:
            return False
        return True
    
    def newfile(self,version):
        if self.exists(r'C:\Program Files (x86)\Microsoft Office\Office14\EXCEL.EXE'):
            path2010 = 'C:\\Program Files (x86)\\Microsoft Office\\Office14\\EXCEL.EXE'
        elif self.exists(r'C:\Program Files\Microsoft Office\Office14\EXCEL.EXE'):
            path2010 = 'C:\\Program Files\\Microsoft Office\\Office14\\EXCEL.EXE'
        else:
            path2010=''
        
        if self.exists(r'C:\Program Files (x86)\Microsoft Office\Office15\EXCEL.EXE'):
            path2013 = 'C:\\Program Files (x86)\\Microsoft Office\\Office15\\EXCEL.EXE'
        elif self.exists(r'C:\Program Files (x86)\Microsoft Office 15\root\Office15\EXCEL.EXE'):
            path2013 = 'C:\\Program Files (x86)\\Microsoft Office 15\\root\\Office15\\EXCEL.EXE'
        else: #self.exists(r'C:\Program Files\Microsoft Office\Office15\EXCEL.EXE'):
            path2013 = 'C:\\Program Files\\Microsoft Office\\Office15\\EXCEL.EXE'
      
        proper = {
            'excel2010':path2010,
            'excel2013':path2013,
            'LotusServerFile': '-'
            
        }
        f = open('%s%s-prop.dat' % (settings['путь_к_настройкам'], getpass.getuser()),"wb")
        pickle.dump(proper, f)
        f.close
    
    @staticmethod
    def load_proper():
        f = open('%s%s-prop.dat' % (settings['путь_к_настройкам'], getpass.getuser()),"rb")
        proper = pickle.load(f)
        # print(cards)
        return (proper)
    @staticmethod
    def save_proper(crd):
        f=open('%s%s-prop.dat' % (settings['путь_к_настройкам'], getpass.getuser()), 'wb')
        pickle.dump(crd, f)
        f.close
    
        
    
class Infodict:
    # словарь для общих настроек, не зависящих от того или иного пользователя
    def newfile_Info(self):
        infoDesc = {
            'Version': 0.001,
            'Резервный_Сервер': "10.252.45.177",
            # в файле - в базе
            'АисИНФО': [0,0,0],
            '106ИНФО': [["Борщ",0,0]],
            'btn_106-затрачено':[0,0],
            'btn_107-затрачено':[0,0],
            'Sroki_Svod_btn-затрачено':[0,0],
            'All_bez_back-затрачено':[0,0],
            'Prosrozka_btn-затрачено':[0,0],
            'Matrica_btn-затрачено':[0,0],
            'BLACK_Q_btn-затрачено':[0,0],
            'BIG_GREEN_btn-затрачено':[0,0],
            'vsesrazu-затрачено':[0,0],
            'btn_25-затрачено':[0,0],
            'BIG_ZAP-затрачено':[0,0],
            'BIG_SREZ-затрачено':[0,0],
            'reservButton-затрачено':[0,0],
            'btn_106_fc-затрачено':[0,0],
            'renew_kkt-затрачено':[0,0],
            'kktnalog-затрачено':[0,0],
            'AIS_btn-затрачено':[0,0],
            '106ИНФО-время':1,
            'резервное-время': datetime.date(2020,12,1),
            '101лягушка': 0,
            '101лягушкастар': 0,
            'СрокиЛягушка': 0,
            'СрокиЛягушкастар': 0,
            'БезбэкЛягушка': 0,
            'БезбэкЛягушкастар': 0,
            'Последний25': datetime.date(2020,1,1)
        }
        f = open(settings['путь_к_общей_инфе'],"wb")
        pickle.dump(infoDesc, f)
        f.close
    @staticmethod
    def load_info():
        f = open(settings['путь_к_общей_инфе'],"rb")
        infoDesc = pickle.load(f)
        # print(cards)
        return (infoDesc)
    @staticmethod
    def save_info(crd):
        f=open(settings['путь_к_общей_инфе'], 'wb')
        pickle.dump(crd, f)
        f.close