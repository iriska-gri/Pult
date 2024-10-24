import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem 
from PyQt5.QtCore import QDateTime, Qt, QThread, QUrl, QPropertyAnimation, QRect
import random
import design  # Это наш конвертированный файл дизайна
import loadprops
from unt import Ui_date_for_107 as dateform107
from handprop import Ui_Dialog as handprop
from upload import Ui_RestoreCSV as uploadF
from newversion import Ui_newversiondialog as newversion
from kkt import Ui_kkt4period as kkt4period
from error import Ui_error as error
import subprocess
import math
from datetime import datetime, time,timedelta
from config.orm import Orm
import pandas as pd
import numpy as np
import traceback
from datetime import datetime, time, timedelta, date
from pathlib import Path
import webbrowser
from config.settings import settings, diftext
import zipfile
import getpass
import chardet
from config.kktokvedinfo import kktokvedinfo
from completed import Ui_finished as finished
from anysheet import IcheckForPicture
err = ''
clicked = ''
fileNames=''
dt=''
calendar=''
end_date=''
chkstate=False
checkBox106var= True
class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow,QtWidgets.QFileDialog, loadprops.Properties, loadprops.Infodict,dateform107):
    
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        
        super().__init__()
        try:
            
            self.proper = self.load_proper()
            
        except FileNotFoundError:
            self.newfile(settings['Version'])
            
            self.proper = self.load_proper()
        if Path(settings['путь_к_общей_инфе']).exists()==False:
            self.newfile_Info()

        try:
            infodesc = self.load_info()
            if settings['Version']< infodesc['Version']:
                print("ОБНОВИСЬ")
                print(str(infodesc['Version']) + '-обновись-'+ str(settings['Version']))
                dialog = QtWidgets.QDialog()
                dialog.ui = newversion()
                dialog.ui.setupUi(dialog)
                dialog.ui.novation.setSource(QUrl.fromLocalFile(settings['обновления']))
                dialog.ui.letmedown.clicked.connect(self.givemenewversion)
                dialog.ui.label_2.setPixmap(QtGui.QPixmap(settings["путь_к_картинкам"]+"MarioNovation.png"))
                dialog.exec_()  
            elif infodesc['Version'] < settings['Version']: 
                infodesc['Version'] = settings['Version']
                self.save_info(infodesc)
                print(str(infodesc['Version']) + '-у меня новее не надо-' + str(settings['Version']))
        except FileNotFoundError:
            self.newfile_Info(settings['Version'])
            print(str(infodesc['Version']) + '-создал-' + str(settings['Version']))
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        print(str(infodesc['Version']) + '-мимо' + str(settings['Version']))
        self.progressBar.hide()
        self.mythread = MyThread()
        self.getdate_from_calendar107(self.calendar107.selectedDate().toString("yyyy-MM-dd"))
        for x in settings['кнопкиЭксель']: #Вешаем на кнопки действия
            getattr(self, x).clicked.connect(lambda:self.openexcel(self.sender().objectName()))
        for x in settings['кнопкипроцедуры']:
            getattr(self, x).clicked.connect(lambda:self.on_clicked(self.sender().objectName())) 
        icon = QtGui.QIcon()

        icon.addPixmap(QtGui.QPixmap(settings["путь_к_картинкам"]+"ico.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)  
        self.setWindowIcon(icon)
        self.checkBox106.clicked.connect(self.check)
        self.checkallTime.clicked.connect(self.rennovation)
        self.tableWidget101.setColumnWidth(0, int(self.tableWidget101.width()*0.8)) 
        self.tableWidget101.setColumnWidth(1, int(self.tableWidget101.width()*0.15)) 
        self.changedinfo.setColumnWidth(0, int(self.changedinfo.width()*0.5)) 
        self.changedinfo.setColumnWidth(0, int(self.changedinfo.width()*0.4)) 
        self.smile.hide()
        self.smile.setPixmap(QtGui.QPixmap(settings["путь_к_картинкам"]+"smile.png"))
        self.label.setPixmap(QtGui.QPixmap(settings["путь_к_картинкам"]+"grog.png"))
        self.label_4.setPixmap(QtGui.QPixmap(settings["путь_к_картинкам"]+"foxnobg.png"))
        print (date.today())
        
        self.rennovation()
        self.LinkBox.activated.connect(lambda:self.deflinkBox(self.LinkBox.currentIndex()))  
        self.calendar107.selectionChanged.connect(lambda:self.getdate_from_calendar107(self.calendar107.selectedDate().toString("yyyy-MM-dd")))
        self.btn_106.clicked.connect(lambda:self.fileDial(self.sender().objectName()))
        self.btn_106_fc.clicked.connect(lambda:self.fileDial(self.sender().objectName()))
        self.btn_107.clicked.connect(lambda:self.open_dialog107(self.sender().objectName()))
        
        # self.btn_107_FKT.clicked.connect(lambda:self.open_dialog107(self.sender().objectName()))
        # self.AIS_btn_FKT.clicked.connect(lambda: self.on_clicked(self.sender().objectName()))
        
        self.btn_25.clicked.connect(lambda:self.fileDial(self.sender().objectName()))
        self.reservButton.clicked.connect(lambda: self.rezbut(self.sender().objectName()))
        self.AIS_btn.clicked.connect(lambda: self.on_clicked(self.sender().objectName()))
        self.mythread.started.connect(self.on_started)
        self.mythread.finished.connect(self.on_finished)
        self.mythread.mysignal.connect(self.on_change, QtCore.Qt.QueuedConnection)
        self.renew_kkt.clicked.connect(lambda:self.new_kkt(self.sender().objectName(),self.calendar107.selectedDate()))
        self.kktnalog.clicked.connect(lambda:self.new_kkt(self.sender().objectName(),self.calendar107.selectedDate().toPyDate()))
        self.send_daily_stat.clicked.connect(lambda: self.on_clicked(self.sender().objectName()))
        self.label.mousePressEvent=self.froggy
        self.label_4.mousePressEvent=self.foxydelkkt
        # тест окна
        self.andreeva.clicked.connect(lambda: self.on_clicked(self.sender().objectName()))
     
# #Верхнее меню
        self.action_107_recalc.triggered.connect(lambda: self.on_clicked(self.sender().objectName()))
        self.action_107_del.triggered.connect(lambda:self.open_dialog107(self.sender().objectName()))
        self.action101.triggered.connect(lambda: self.on_clicked(self.sender().objectName()))
        self.calren.triggered.connect(self.rennovation)
        self.propWindow.triggered.connect(self.prophand)
        self.option_drop.triggered.connect(self.properdrop)
        self.restore_csv.triggered.connect(self.Restoredb)
        
        self.kktperiod.triggered.connect(self.open_kktwid)

    def open_kktwid(self,btnName):
        dialog = QtWidgets.QDialog()
        dialog.ui = kkt4period()
       
        dialog.ui.setupUi(dialog)
        dialog.ui.date_end.setDateTime(QtCore.QDateTime(QtCore.QDate.currentDate(), QtCore.QTime(1, 0, 0)))
        
        dialog.ui.kkttozip.clicked.connect(lambda:self.new_kkt(self.sender().objectName(),dialog.ui.kkt_date_start.date().toPyDate(),dialog.ui.date_end.date().toPyDate()))
        dialog.ui.kktto38.clicked.connect(lambda:self.new_kkt(self.sender().objectName(),dialog.ui.kkt_date_start.date().toPyDate(),dialog.ui.date_end.date().toPyDate()))
        dialog.exec_()   
    def froggy(self,pxm):
        self.on_clicked('action101')         
    def foxydelkkt(self,pxm):
        self.open_dialog107('action_107_del')
        
    def new_kkt(self,btnName,cal_date,enddate=''):
        global calendar,end_date
        calendar=cal_date
        end_date = enddate
        self.on_clicked(btnName)
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_F5:
            print ("Пошел на обновление")
            self.rennovation()
    def givemenewversion(self):
        thisfile = "%s" %(sys.argv[0])
        subprocess.Popen('%s "%s" "%s"' %(settings["батниккиллер"], thisfile, settings["новыйФайл"]))
        sys.exit()

    def check(self):
        global checkBox106var
        if self.checkBox106.checkState():
            checkBox106var=True
        else:
            checkBox106var=False
       
            
    def on_clicked(self, btnName):
        global clicked
        clicked = btnName
        self.AIS_btn.setDisabled(True) # Делаем кнопку неактивной
        self.mythread.start()         # Запускаем поток
        self.statusBar().showMessage("Начинается загрузка")
        global err
        global start_time
        err=''
        start_time=datetime.now()
    def on_started(self):	# Вызывается при запуске потока
        
        self.progressBar.show()  
        self.progressBar.setProperty("value",0)
    def on_finished(self):      # Вызывается при завершении потока
        self.statusBar().showMessage("Готово")
        self.AIS_btn.setDisabled(False) # Делаем кнопку активной
        self.progressBar.hide()
        self.statusBar().showMessage("")
        self.rennovation()
        global err
        global clicked
        global fileNames
        print(clicked)
        newest_time = datetime.now()
        if err=="":
            if clicked in ["btn_107","action_107_del"]:
                self.getdate_from_calendar107(self.calendar107.selectedDate().toString("yyyy-MM-dd"))
            dialog = QtWidgets.QDialog()
            dialog.ui = finished()
            dialog.ui.setupUi(dialog)
            dialog.ui.pushButton.clicked.connect(dialog.close)
            dialog.ui.block.setPixmap(QtGui.QPixmap(settings["путь_к_картинкам"]+"block.png"))
            dialog.ui.mario.setPixmap(QtGui.QPixmap(settings["путь_к_картинкам"]+"mariooknobg.png"))
            InfoDict = self.load_info() 
            try:    
                dialog.ui.old_time.setText(str(InfoDict['{}-затрачено'.format(clicked)][0]))
                InfoDict['{}-затрачено'.format(clicked)][0]= newest_time-start_time
                dialog.ui.new_time.setText(str(InfoDict['{}-затрачено'.format(clicked)][0]))
                
                self.save_info(InfoDict)
            except Exception:
                print("Возможно, что действие не отслеживается")
            if fileNames:
                dialog.ui.filenamessag.setText("Залитый файл: {}".format(fileNames[0]))
            dialog.ui.messagefinish.setText("Операция по %s Выполнена успешно!!!!" %diftext[clicked][random.randint(0, len(diftext[clicked])-1)])
            animation = QPropertyAnimation(dialog.ui.mario, b"geometry")
            animation2 = QPropertyAnimation(dialog.ui.messagefinish, b"geometry")
            animation.setLoopCount(800)
            animation2.setLoopCount(800)
            animation.setDuration(5000)
            animation2.setDuration(5000)
            animation.setStartValue(QRect(-60,90, 51, 61))
            animation2.setStartValue(QRect(70,50,0,0))
            animation.setKeyValueAt(0.01,QRect(-60,90,51,61))
            animation.setKeyValueAt(0.18,QRect(60,90,51,61))
            animation2.setKeyValueAt(0.22,QRect(70,50,0,0))
            animation.setKeyValueAt(0.22,QRect(60,75,51,61))
            animation2.setKeyValueAt(0.25,QRect(70,20,550,21))
            animation.setKeyValueAt(0.25,QRect(60,90,51,61))
            animation2.setKeyValueAt(0.55,QRect(70,20,550,21))
            animation.setEndValue(QRect(850,90, 51, 61))
            animation2.setEndValue(QRect(70,20,550,21))
            # dialog.ui.messagefinish.setText("")
            animation.start()
            animation2.start()
            dialog.exec_() 
            clicked=""
            fileNames=''
                    
        elif len(err)>0:
            dialog = QtWidgets.QDialog()
            dialog.ui = error()
            dialog.ui.setupUi(dialog)
            dialog.ui.textBrowser.setPlainText(err)
            dialog.ui.okButton.clicked.connect(dialog.reject)
            dialog.exec_()  
            err=""
    def on_change(self, s): #Изменения в потоке. Текст и прогресс
        self.progressBar.setProperty("value",s.split("--")[0])
        if clicked=="AIS_btn":
            self.FileAisInfo_base.display(int(s.split("--")[1]))
        elif clicked in ("btn_106",'btn_106_fc',"soonDump","reservButton", "btn_107","Upload","btn_25","kktnalog",'kktto38'):
            self.statusBar().showMessage(s.split("--")[1])
    def rezbut(self, btnName):   
        self.statusBar().showMessage("Дамп БД")
        self.on_clicked(btnName)
    def getdate_from_calendar107(self, cal_date):
        orm_ = Orm()
        dateinfo=orm_.select_date_for_107(cal_date,0)
        returndate=""
        for x in dateinfo:
            returndate = returndate + x[0].strftime("%H:%M") + "  "
        if len(returndate)==0:
            returndate="В базе данных нет информации по %s" %(cal_date)
        orm_.connclose() 
        self.text107Time0.setText(returndate) 
    
    def checkstate(self):
        global chkstate
        chkstate= self.checkallTime.checkState()
        
    def rennovation(self): #Обновление всех данных в окне
        self.prazdn.setPixmap(QtGui.QPixmap(settings["путь_к_картинкам"]+"prazdn{}.png".format(IcheckForPicture())))
        orm_ = Orm()
        InfoDict = self.load_info() 
        self.kktinf = kktokvedinfo()
        # показ картинки когда все хорошо по оквэд и ккт
        # if self.kktinf[1]:
            # self.smile.show()

        # else:
            # self.smile.hide()

        self.kkText.setText(self.kktinf[0])
        self.FileAisInfo.display(InfoDict["АисИНФО"][0]) 
        self.FileAisInfo_base.display(InfoDict["АисИНФО"][1]) 
        self.reserv_adress.setText(InfoDict["Резервный_Сервер"]) 
        self.date106Info.setText(str(InfoDict["106ИНФО-время"]))
        self.AisInfo.setText(str(InfoDict['АисИНФО'][2])[:-7])
        self.tableWidget101.setRowCount(len(InfoDict["106ИНФО"]))
        self.adinf.setText(str(InfoDict['101лягушка']))
        self.SROKINF.setText(str(InfoDict['СрокиЛягушка']))
        self.ABinf.setText(str(InfoDict['БезбэкЛягушка']))
        self.adinf_2.setText(str(InfoDict['101лягушка']-InfoDict['101лягушкастар']))
        self.SROKINF_2.setText(str(InfoDict['СрокиЛягушка']-InfoDict['СрокиЛягушкастар']))
        self.ABinf_2.setText(str(InfoDict['БезбэкЛягушка']-InfoDict['БезбэкЛягушкастар']))
        self.blue_submit.setText(str(InfoDict['Последний25']))
        self.checkstate()
        self.labelchanged.setText("Что поменялось с %s" %datetime.strftime(InfoDict['резервное-время'],"%Y-%m-%d %H:%M:%S"))
        for  i in range(len(InfoDict["106ИНФО"])):
            
            self.tableWidget101.setItem(i, 0, QTableWidgetItem(str(InfoDict["106ИНФО"][i][0])))
            self.tableWidget101.setItem(i,1, QTableWidgetItem(str(InfoDict["106ИНФО"][i][1])))
            rezervator = orm_.infodump(InfoDict['резервное-время'],self.checkallTime.checkState())
        
        self.changedinfo.setRowCount(len(rezervator))
        
        for  i in range(len(rezervator)):
            self.changedinfo.setItem(i, 0, QTableWidgetItem(str(rezervator[i][1])))
            self.changedinfo.setItem(i,1, QTableWidgetItem(str(rezervator[i][2])))
        orm_.connclose()
    def prophand(self):
        proper = self.load_proper()
        dialog = QtWidgets.QDialog()
        dialog.ui = handprop()
        dialog.ui.setupUi(dialog)
        dialog.ui.excel2010edit.setText(str(proper['excel2010']))
        dialog.ui.excel2013edit.setText(str(proper['excel2013']))
        dialog.ui.lotusNotes.setText(str(proper['LotusServerFile']))
        dialog.ui.excel2010.clicked.connect(lambda:self.fileDial(self.sender().objectName(),dialog.ui.excel2010edit))
        dialog.ui.excel2013.clicked.connect(lambda:self.fileDial(self.sender().objectName(),dialog.ui.excel2013edit))
        dialog.accepted.connect(lambda: self.acceptedprop(dialog.ui.lotusNotes.text()))
        dialog.exec_()  
    def acceptedprop(self, prop3):
            proper = self.load_proper()
            proper['LotusServerFile']= prop3
            self.save_proper(proper)
    def Restoredb(self):
        
        dialog = QtWidgets.QDialog()
        dialog.ui = uploadF()
        dialog.ui.setupUi(dialog)
        dialog.ui.lookup.clicked.connect(lambda:self.fileDial(self.sender().objectName(),dialog.ui.filename))
        dialog.ui.Upload.clicked.connect(lambda:self.restoreUpload(self.sender().objectName(),dialog.ui.basename.text(),dialog.ui.tablename.text(),dialog.ui.filename.text(),dialog))
        dialog.exec_() 


    def properdrop(self):
        Path('%s%s-prop.dat' % (settings['путь_к_настройкам'], getpass.getuser())).unlink()
        self.newfile(settings['Version'])
        self.rennovation()
    def deflinkBox(self,indexlink):
        webbrowser.get(using=None).open_new_tab(settings["ссылки"][indexlink])
   
    def open_dialog107(self,btnName): #Заливка отчета 107. Диалоговое окно для выбора даты
        orm_=Orm()
        dialog = QtWidgets.QDialog()
        dialog.ui = dateform107()
        dialog.ui.setupUi(dialog)
        dialog.ui.dateTimeEdit_107.setDateTime(QtCore.QDateTime(orm_.select_date_for_107(None,1)[0]))
        dialog.accepted.connect(lambda: self.acceptedDt(dialog.ui.dateTimeEdit_107,btnName))
        orm_.connclose() 
        dialog.exec_()      
        
    def acceptedDt(self,datetime107,btnName): #Сохранение даты 107 и запуск выбора файла
        global dt
        dt= datetime107.dateTime()
        dt = dt.toString(Qt.ISODate)
       
        if btnName in ["btn_107"]:
            self.fileDial(btnName)
        elif btnName=="action_107_del":
            self.on_clicked(btnName)
    def restoreUpload(self,btnName,basename,tablename,filename,dialog):
        global clicked
        clicked = btnName
        global fileNames
        fileNames = filename
        global dt
        dt = "%s.%s" %(basename,tablename)
        self.on_clicked(btnName)
        dialog.close()

    def fileDial(self,btnName, windoww=0): #Окно файлового диалога. Возможность выбора одного или нескольких файлов
        pathhome = Path.home()
        if btnName in ["btn_107","btn_25"]:
            name = QtWidgets.QFileDialog.getOpenFileName(None, 'Выбор файла', str(pathhome.joinpath('Desktop')),) 
            
        elif btnName in ["btn_106", "btn_106_fc"]:
            name = QtWidgets.QFileDialog.getOpenFileNames(None, 'Выбор файла',str(pathhome.joinpath('Desktop')),) 
        elif btnName=="lookup":
            name = QtWidgets.QFileDialog.getOpenFileName(None, 'Выбор файла',str(pathhome.joinpath('Desktop')),)
            windoww.setText(str(name[0]))
            return
        elif btnName in ['excel2010','excel2013']:
            proper = self.load_proper()
            proper[btnName]= QtWidgets.QFileDialog.getOpenFileName(None, 'Выбор файла %s' %btnName, str(pathhome.joinpath('Desktop')),)[0] 
            
            windoww.setText(proper[btnName])
            self.save_proper(proper)
            return
        if len(name[0])>0 :
            global fileNames
            fileNames=name[0]
            self.on_clicked(btnName)
           

    #    Функция которая открывает эксель в соответствии с нажатой кнопкой
    def openexcel(self, btnName):
        proper = self.load_proper()
        buttonlist=['btn_2013','prosrozka_exc','black_q_exc','spy_min_exc','otchet2859198','priloj_4','priloj_4_srez','btn_reestr']
        fileList = [settings["Дашборд2013"],settings["Просрочка"],settings["ЧерныйДб"],settings["Шпион"],settings["2859198"],
        settings["Прил4"],settings["Прил4срез"],settings["Реестр"]]
        i = buttonlist.index(btnName)
        subprocess.Popen('"%s" "%s"' % (proper['excel2013'], fileList[i]),shell=True)
 
class MyThread(QtCore.QThread, loadprops.Infodict):
    mysignal = QtCore.pyqtSignal(str)

    def  __init__(self,parent=None):
        QtCore.QThread.__init__(self, parent)
    def distinctTable(self, basename,tblname, orm_):
        self.mysignal.emit("%s--%s" % ("0", "Придется подождать еще. Я не завис. Создаю дистинкт-копию таблицы all_data") )
        orm_.randomQuery("CREATE TABLE {0}.all_data_copyco LiKE {0}.{1}".format(basename,tblname), False)
        orm_.randomQuery("INSERT INTO {0}.all_data_copyco SELECT DISTINCT * FROM {0}.{1}".format(basename,tblname), False)
        self.mysignal.emit("%s--%s" % ("25", "Придется подождать еще. Я не завис. Очистка старой all_data") )
        orm_.randomQuery("DROP TABLE {0}.{1}".format(basename,tblname), False)
        self.mysignal.emit("%s--%s" % ("50", "Придется подождать еще. Я не завис. Заливаю красивые чистые данные в all_data") )
        orm_.randomQuery("RENAME TABLE {0}.all_data_copyco to {0}.{1}".format(basename,tblname), False)

    def encode_Control(self,filename):
        try:
            f = open(filename, 'rb')
            data = f.read()

            for x in ['cp1251','utf-8']:
                try:
                    data.decode(x)
                    return x
                except:
                    print('Ошибка')
                    continue
            f.close()
            return ''
        except Exception:
            
            if self.get_file_size(filename)> 1073741824 and clicked in ["btn_106_fc","btn_106"]:
                return 'cp1251'
    
    def convertTime(self,t):
        if t in ['', 'NULL']:                                
            # return r"\N"
            return "1900-01-01 00:00:00"
        else:
            t1 = t.split()
            a = t1[0].split('.')
            a[0], a[2] = a[2], a[0]
            t3 = '-'.join(a) + ' ' + t1[1]    
            return t3
    def convertTimeNew(self,t,x):
        if t in ['',' ' 'NULL',r"\N"]:                                
            if x in[13,14]:
                return r"\N"
            else:
                return "1900-01-01 00:00:00"
        else:
            # москва
            # if x not in[13,14]:
            #     t1 = t.split(' +')
            #     tdate = datetime.strptime(t1[0], '%d.%m.%Y %H:%M:%S')
            
            #     # print(t1[1].split(':'))
            #     hours, minutes = map(int, t1[1].split(':'))
            #     return tdate-timedelta(hours=(hours-3),minutes=minutes) 
            # else:
            #     return datetime.strptime(t, '%d.%m.%Y %H:%M:%S')
            t1 = t.split()
            a = t1[0].split('.')
            a[0], a[2] = a[2], a[0]
            t3 = '-'.join(a) + ' ' + t1[1]    
            return t3


    def get_file_size(self,file):
        size = Path(file).stat().st_size
        return size
    def remove_values_from_list(self,the_list, val):
        while val in the_list:
            the_list.remove(val)
    
    def run(self):
        try:
            orm_ = Orm()
            if clicked =="AIS_btn": # Функция загрузки АИС. Обрабатывает и заливает данные по нажатию на кнопку
                # orm_.trunc("BlackBerry","ais")
                # df = pd.read_excel(settings["АИС"],header=None, dtype=str, na_values='NULL',keep_default_na=False, skiprows=1) #номер листа с 0
                # df[16]="Последний"
                # lenofdf = df.shape[0]
                # filestr =   str(Path(settings["АИС"]).parent.joinpath("ais.csv"))
                # df.to_csv(filestr, sep=';',quoting = 1, mode='w', header=False, index=False)
                # self.mysignal.emit("%s--%s" % (str(50), str(0)))   
                # orm_.load_local(filestr,"BlackBerry.ais")
                # orm_.commit_to()
                # self.mysignal.emit("%s--%s" % (str(50), str(lenofdf)))  
                # Path(filestr).unlink()     
                orm_.trunc("Sroki_svod","a_AIS")
                
                from load106foreign import give_me_foreign_keys,updateforeign_and_go,addforeign_tsn
                dfstatus = give_me_foreign_keys("id_status_obrabotki, status_obrabotki","Sroki_svod.sprav_ais_status_obrabotki",orm_)
                dfpriznak = give_me_foreign_keys("id_prisnak_statusa_obrabotki, prisnak_statusa_obrabotki","Sroki_svod.sprav_ais_prisnak_statusa_obrabotki",orm_)
                dfSooNstat =  give_me_foreign_keys("id_status_v_SOON, status_v_SOON","Sroki_svod.sprav_ais_status_v_SOON",orm_)
                df = pd.read_excel(settings["АИС"],header=None, dtype=str, na_values='NULL',keep_default_na=False, skiprows=1) #номер листа с 0
                df = df.drop(columns=[0,1,2,4,5,7,12,13,14], axis=1)
                for row in df.values:
                    for x in range(len(row)):
                        row[x]=row[x].strip()
                df[16]=4
                lenofdf = df.shape[0]
                df, dfstatus = updateforeign_and_go(df,dfstatus, 9,0,'Sroki_svod.sprav_ais_status_obrabotki','status_obrabotki','id_status_obrabotki, status_obrabotki',[0,1],orm_)
                df, dfpriznak = updateforeign_and_go(df, dfpriznak, 10, 0,'Sroki_svod.sprav_ais_prisnak_statusa_obrabotki','prisnak_statusa_obrabotki',"id_prisnak_statusa_obrabotki, prisnak_statusa_obrabotki",[0,1],orm_)
                df, dfSooNstat = updateforeign_and_go(df, dfSooNstat, 11, 0,'Sroki_svod.sprav_ais_status_v_SOON','status_v_SOON',"id_status_v_SOON, status_v_SOON",[0,1],orm_)
                
                filestr =   str(Path(settings["АИС"]).parent.joinpath("ais.csv"))
                df.to_csv(filestr, sep=';', quoting = 1, mode='w', header=False, index=False)
                self.mysignal.emit("%s--%s" % (str(50), str(0)))   
                orm_.load_local(filestr,"Sroki_svod.a_AIS")
                orm_.commit_to()
                self.mysignal.emit("%s--%s" % (str(50), str(lenofdf)))  
                Path(filestr).unlink()
                InfoDesc = self.load_info()
                InfoDesc['АисИНФО'][0]=lenofdf
                InfoDesc['АисИНФО'][1]=orm_.countTable("Sroki_svod.a_AIS")[0]
                InfoDesc['АисИНФО'][2]=datetime.now()
                self.save_info(InfoDesc)
                
            # elif clicked =="btn_107": #Заливашка 107
            #     name= fileNames 
            #     if Path(name).suffix != '.csv':
            #         df = pd.read_excel(name,dtype=str,na_values='NULL',keep_default_na=False)
            #     else:
            #         self.mysignal.emit("%s--%s" % (str(1), "Открываю файлик и смотрю что там за кодировочка..."))
            #         whatcode = self.encode_Control(name)
            #         df = pd.read_csv(name, sep=';',na_values='NULL',keep_default_na=False,encoding=whatcode,dtype=str)
            #     print(df.columns[0])    
            #     if len(df.columns)>11: 
            #     # or df.columns[0]!='REGISTRATION_NUMBER':
            #         df = df.drop(df.columns[0], axis='columns')
            #     orm_.trunc("107_gen_ci","all_data_107")
            #     filestr =   str(Path(name).parent.joinpath("new_file_107.csv"))
            #     df.to_csv(filestr, sep=';', mode='w', header=False, index=False)
            #     self.mysignal.emit("%s--%s" % (str(50), "Идет загрузка"))    
            #     orm_.load_local(filestr,"107_gen_ci.all_data_107")
            #     orm_.commit_to()
            #     Path(filestr).unlink()
            #     orm_.insert107_to_full107(dt)
            #     print ("107 залит успешно")

            elif clicked =="action_107_recalc": #пересчет 107 после удаления
                orm_.runproc("Info107Full")
            elif clicked=="action_107_del":
                self.mysignal.emit("%s" % 80) 
                orm_.delfrom107(dt)
            





            elif clicked =="btn_106":
                name= fileNames 
                for name in fileNames:
                   
                    i=1
                    filestr =   str(Path(name).parent.joinpath("new_file_.csv"))
                    whatcode = self.encode_Control(name)
                    for chunk in pd.read_csv(name, sep=';', header=None, na_values='NULL',keep_default_na=False, dtype=str,chunksize=10000, engine='python', encoding=whatcode):
                        chunk = chunk.drop(columns=[7,13,14,17,19,20,25])
                        for row in chunk.values:
                            if row[1]=='SENT':
                                row[0]= f"-{row[0]}"
                            if row[17] in ['','-1']:
                                row[17]='35100'
                            for x in [8,9,10,11,13,14,20]:
                                row[x] = self.convertTime(row[x])   

                        chunk.to_csv(filestr, sep=';', quoting = 1, mode='a', header=False, index=False)
                        self.mysignal.emit("%s--%s" % (str(i), "Идет обработка файла. 1% - это 10000 строк. Не отражает реальные %") )   
                        i+=1
                    self.mysignal.emit("%s--%s" % ("50", "Загрузка файла на сервер. Не отражает реальные %") )              
                    orm_.load_local(filestr,"101_gen_ci.all_data")
                    orm_.commit_to()
                    self.mysignal.emit("%s--%s" % ("80", "Удаляю подготовленный файл. Не отражает реальные %") ) 
                    Path(filestr).unlink()
                   
                   
                    
                      
                 
                
                if checkBox106var:
                    self.distinctTable('Sroki_svod','a_all_data_106',orm_)
               
                InfoDesc = self.load_info()
                self.mysignal.emit("%s--%s" % ("99", "Ждите еще немного. Происходит обработка и сортировка полученной информации для отображения на панели пульта") )
                InfoDesc['106ИНФО']=orm_.randomQuery("SELECT DISTINCT(Sroki_svod.a_all_data_106.life_situation_name) as lsn, (select COUNT(distinct(a_all_data_106.card_id)) FROM Sroki_svod.a_all_data_106 where life_situation_name=lsn) As coco FROM Sroki_svod.a_all_data_106 GROUP BY lsn ORDER BY coco DESC",True)
                InfoDesc['106ИНФО-время']= datetime.now()
                sravn = InfoDesc['101лягушка']
                InfoDesc['101лягушка']=orm_.randomQuery("select count(distinct Sroki_svod.a_all_data_106.card_id) from Sroki_svod.a_all_data_106",False)[0]
                if InfoDesc['101лягушка']>sravn:
                    InfoDesc['101лягушкастар']=sravn
                self.save_info(InfoDesc)
            
            elif clicked =="btn_25":
                name= fileNames
                
                from load106foreign import give_me_foreign_keys,updateforeign_and_go,addforeign_tsn
                filestr =   str(Path(name).parent.joinpath("new_file25_.csv"))
                self.mysignal.emit("%s--%s" % ("5", "определяю кодировку") )
                whatcode = self.encode_Control(name)
                itern = 5
                taxcode = give_me_foreign_keys("tax_code, id_nomer_i_naim_reg,id_federal,  inspekcija","Sroki_svod.sprav_regions_svod",orm_)

                dflsn = give_me_foreign_keys("id_life_situation_name, life_lk","Sroki_svod.sprav_life_situation_name",orm_)
                for chunk in pd.read_csv(name, sep=';', na_values=r"\N",keep_default_na=False, dtype=str,chunksize=150000, engine='python', encoding=whatcode,header=None):
                    
                    
                    chunk = chunk.drop(chunk[chunk[0].str.contains(r"IN_NUMBER", na=False)==True].index)
                    chunk = chunk.loc[chunk[9] != '']
                    # print (chunk)
                    chunk2 = chunk[[3,4]]
                    for row in chunk.values:
                                 
                        try:
                            row[9] = datetime.strptime(row[9],'%d.%m.%Y')
                        except Exception:
                            row[9] = datetime.strptime(row[9],'%Y-%m-%d')
                    chunk = chunk.drop(columns=[2,4,6,7,8])
                    
                    
                    chunk, dflsn = updateforeign_and_go(chunk, dflsn, 1,'0_y','Sroki_svod.sprav_life_situation_name','life_lk','id_life_situation_name,  life_lk',['0_y'],orm_)
                    chunk2[3]=chunk2[3].astype(int)
                    chunk2=chunk2.drop_duplicates()
                    if taxcode.size>0:
                    
                        chunktest = chunk2.merge(taxcode,how='left', left_on = 3, right_on=0)
                        chunk2 = chunktest.where(chunktest[0].isnull()==True).drop_duplicates()
                        chunk2 = chunk2.drop(columns=[0,1,2,'3_y'])

                        chunk2.columns = [3,'ls',4]
                    
                    
                    else:
                        print('попался-попался')
                        
                        chunk2.insert(1,"ls",0)
                    chunk2=chunk2.dropna(how='all')
                    chunk2['ls'] =  chunk2[3]/100
                    
                    chunk2['ls']=chunk2['ls'].astype(int)
                    # chunk2.insert(2,"nu",'NULL')
                    taxcodereg = taxcode.drop(columns=[0,3])
                    taxcodereg= taxcodereg.where(taxcodereg[2].isnull()==False).drop_duplicates().dropna(how='all').astype(int)

                    chunk2 = chunk2.merge(taxcodereg,how='left', left_on = 'ls', right_on=1)
                    
                    if chunk2.shape[0]>0:
                        for x in range(chunk2.shape[0]):
                            
                            j = '"{}","{}",{},"{}"'.format(str(chunk2.iloc[x][3]),str(chunk2.iloc[x]["ls"]),'NULL'  if math.isnan(chunk2.iloc[x][2]) else "'" + str(chunk2.iloc[x][2]) + "'" ,str(chunk2.iloc[x][4]))
                            
                            orm_.insert_tofc(j,'Sroki_svod.sprav_regions_svod')
                            orm_.commit_to()
                    
                        taxcode = give_me_foreign_keys("tax_code, id_nomer_i_naim_reg,id_federal,  inspekcija","Sroki_svod.sprav_regions_svod",orm_)    
                        print ("апдейт ключей")
    # Если вдруг понадобятся нулл-значения 
                    # chunk=chunk.replace("",r"\N")
                    # print(chunk)
                       
                    self.mysignal.emit("%s--%s" % (str(itern), "Пошел в обработку. Проценты - не реальные значения") )
                    chunk.to_csv(filestr, sep=';', quoting = 1, mode='w', header=False, index=False,encoding='utf-8')
                    orm_.load_local(filestr,"Sroki_svod.a_all_data_25")
                    orm_.commit_to()
                    Path(filestr).unlink()
                    InfoDesc = self.load_info()
                    InfoDesc['Последний25'] = orm_.randomQuery("select max(RECEIPT_DATE) from a_all_data_25", False)[0]
                    
                    self.save_info(InfoDesc)

            elif clicked =="reservButton":
                import csv
                InfoDesc = self.load_info()
                currentDirectory = Path(settings["путь_в_дамп"])
                
                for currentFile in currentDirectory.glob('*.*'):  
                    if datetime.timestamp(datetime.now())- currentFile.stat().st_mtime>settings['Время_хранения_сек']: 
                        currentFile.unlink()
                print(chkstate)
                whattoupdate = orm_.infodump(datetime.strftime(InfoDesc['резервное-время'],"%Y-%m-%d %H:%M:%S"),chkstate)
                InfoDesc['резервное-время']= datetime.now()
                iterator =0
                print(whattoupdate)
                lenofdf=len(whattoupdate)
                for x in whattoupdate:
                    time4name = datetime.strftime(InfoDesc['резервное-время'],"%Y-%m-%d_%H-%M-%S")
                    zipmanFile = "%s/%s__%s__%s.zip" % (settings["путь_в_дамп"],x[0],x[1], time4name)
                    csvmanFile = "%s/Data_%s__%s__%s.CSV" % (settings["путь_в_дамп"],x[0],x[1],time4name)
                    createFile = "%s/Create_Table%s__%s__%s.txt" % (settings["путь_в_дамп"],x[0],x[1],time4name)
                    if Path(zipmanFile).exists()==False:
                        cursor = orm_.connection.cursor()
                        cursor.execute("SHOW CREATE TABLE %s.%s " %(x[0],x[1]))        
                        with open(createFile, 'w', encoding='utf-8', newline='') as myfile:  
                            data = pd.DataFrame(cursor.fetchone())
                            myfile.write(data[0][1])
                        cursor.execute("Select * FROM %s.%s " %(x[0],x[1]))
                      
                        with open(csvmanFile, 'w', encoding='utf-8', newline='') as myfile:
                            self.mysignal.emit("%s--%s" % (int(100*iterator/(lenofdf*2)), "Создание %s" %csvmanFile))
                            iterator +=1      
                            while True:
                                chunk = pd.DataFrame(cursor.fetchmany(100000))  
                                
                                chunk.to_csv(myfile, sep=';', quoting = 1, mode='a', header=False, index=False)
                                if len(chunk)==0:
                                    break
                        
                        a= zipfile.ZipFile(zipmanFile,mode="a",compression=zipfile.ZIP_DEFLATED)
                        a.write(csvmanFile)
                        a.write(createFile)
                        a.close()
                        Path(csvmanFile).unlink()
                        Path(createFile).unlink()
                        self.mysignal.emit("%s--%s" % (int(100*iterator/(lenofdf*2)), "Архивация файла %s" %zipmanFile))
                        iterator +=1
                self.save_info(InfoDesc)
            
            
            
            # elif clicked =='action101':
                # InfoDesc = self.load_info()
                # a= None
                # a=orm_.randomQuery("select count(distinct Sroki_svod.all_bez_back.card_id) as ABB, (select  count(distinct 101_gen_ci.all_data.card_id) from 101_gen_ci.all_data)  as AD, (select  count(DISTINCT 101_gen_ci.SROKI_SVOD_STAT.card_id) from 101_gen_ci.SROKI_SVOD_STAT) AS SS, (SELECT MAX(RECEIPT_DATE) FROM BLUE_STAT.data_report_25) AS BS from 101_gen_ci.all_bez_back",False)
                # oldy = ['БезбэкЛягушкастар','101лягушкастар','СрокиЛягушкастар']
                # i=0
                
                # for x in oldy:
             
                #     print(InfoDesc[x],InfoDesc[x[:-4]],a[i])
                #     if int(a[i])!= int(InfoDesc[x[:-4]]):
                #         print("условия выполнены")
                #         InfoDesc[x],InfoDesc[x[:-4]]=InfoDesc[x[:-4]],a[i]
                #     i+=1
                    
                # InfoDesc['Последний25'] = a[3]   
                # self.save_info(InfoDesc)


            elif clicked in settings['кнопкипроцедуры']:
                
                whattorun =  settings['кнопкипроцедуры'].index(clicked)   
                orm_.runproc(settings['процедуры'][whattorun])
               
                orm_.commit_to()
                
                if whattorun <2:
                    InfoDesc = self.load_info()
                    if whattorun==1:
                        InfoDesc['СрокиЛягушка']=orm_.randomQuery("select count(DISTINCT Sroki_svod.SROKI_SVOD_STAT.card_id) from Sroki_svod.SROKI_SVOD_STAT",False)[0]
                    # else:
                    #     InfoDesc['БезбэкЛягушка']=orm_.randomQuery("select count(distinct Sroki_svod.all_bez_back.card_id) from 101_gen_ci.all_bez_back",False)[0]
                    self.save_info(InfoDesc)
            elif clicked=="send_daily_stat":
                from ejstat import excelandsend, send_mail,excel_catch_screen
                excelandsend()
            
            elif clicked == 'Upload':

                # start_time = time.time()
                cursor = orm_.connection.cursor()
                name= fileNames 
                cursor.execute("TRUNCATE %s" %(dt))
                orm_.commit_to()
                i=0  
                                      
                if self.get_file_size(name)> 1073741824:
                    cursor.execute(f"SHOW INDEX FROM {dt} Where Key_name not LIKE 'FK_%%'")
                    tableinfo = pd.DataFrame(cursor.fetchall())   
                    tableinfo.sort_values(2,inplace=True)
                    keyNames = tableinfo[2].unique()
                    if len(keyNames)>0:
                        dropstr = "ALTER TABLE %s" %dt
                        dropindex=""
                    
                        for el in keyNames:
                            if el!="PRIMARY":  
                                dropindex = dropindex + " DROP INDEX `%s`,"%el
                        dropstr = dropstr + dropindex[:-1]                   
                        cursor.execute(dropstr)
                        orm_.commit_to()
                    print('сбросил')
                filestr =   str(Path(name).parent.joinpath("short_new_file_.csv"))

                for chunk in pd.read_csv(name, sep=';', header=None, na_values='NULL',keep_default_na=False, dtype=str,chunksize=500000, encoding='utf-8'):
                    chunk=chunk.replace("",r"\N")
                    chunk.to_csv(filestr, sep=';', quoting = 1, mode='w', header=False, index=False)
                    
                    orm_.load_local(filestr,dt)
                    orm_.commit_to()
                    i+=1
                    self.mysignal.emit("%s--%s" % (str(int(i)), "Идет загрузка. 1% - это 500000 строк. Не отражает реальные %") )
                    
                Path(filestr).unlink()
                if self.get_file_size(name)> 1073741824:
                    self.mysignal.emit("%s--%s" % (str(80), "Возвращаю ключи на место. Не отражает реальные %") )
                    if len(keyNames)>0:
                        addkeystr = 'ALTER TABLE %s'%dt
                        for el in keyNames:
                            if el!="PRIMARY": 
                                filtered=tableinfo.where(tableinfo[2]==el, other='NULL')
                                col_one_list = filtered[4].tolist()
                                uniqlist = filtered[1].tolist()
                                self.remove_values_from_list(uniqlist,'NULL')
                                self.remove_values_from_list(col_one_list,'NULL')
                            
                                if uniqlist[0]==1:
                                    twistlist = ' ADD INDEX `%s` (%s),'%(el,str(col_one_list).strip('[]'))            
                                else:
                                    twistlist = ' ADD UNIQUE INDEX `%s` (%s),'%(el,str(col_one_list).strip('[]'))
                                twistlist=twistlist.replace("'","`")
                                addkeystr = addkeystr + twistlist
                        addkeystr=addkeystr[:-1]
                        cursor.execute(addkeystr)
                        orm_.commit_to()
                    print('восстановил')
                # print("--- %s seconds ---" % (time.time() - start_time)) 
            

            elif clicked in['renew_kkt','kktto38']:
                from okved import upload_datakkt
                global calendar,end_date
                if clicked == 'renew_kkt':
                    upload_datakkt(calendar.toString("yyyy-MM-dd"))
                else:
                    i=0
                    while calendar <= end_date:
                        s=datetime.strftime(calendar,"%Y-%m-%d")
                        upload_datakkt(s)
                        print("есть {}".format(calendar))
                        calendar+=timedelta(days=1)
                        i+=1
                        self.mysignal.emit("%s--%s" % (str(i), "1% =1 загруженный день...") )
                        
                calendar,end_date='',''
            #  ------------------------------------------------------------------------- 107 FKT   
            elif clicked == 'btn_107':
                from load106foreign import give_me_foreign_keys,updateforeign_and_go,addforeign_tsn
                orm_ = Orm()
                dfcategory = give_me_foreign_keys("id_object_category, object_category","Sroki_svod.sprav_object_category",orm_)

                dftitle = give_me_foreign_keys("id_life_situation_name, life_situation_name","Sroki_svod.sprav_life_situation_name",orm_)
                tsn =  give_me_foreign_keys("task_step_id, task_step_name","Sroki_svod.sprav_task_step_name",orm_)
                name= fileNames 
                if Path(name).suffix != '.csv':
                    df = pd.read_excel(name,dtype=str,na_values=r'\N',keep_default_na=False)
                else:
                    self.mysignal.emit("%s--%s" % (str(1), "Открываю файлик и смотрю что там за кодировочка..."))
                    whatcode = self.encode_Control(name)
                    df = pd.read_csv(name, sep=';',na_values=r'\N',keep_default_na=False,encoding=whatcode,dtype=str,header=None,)
                    
                if len(df.columns)>11: 
                # or df.columns[0]!='REGISTRATION_NUMBER':
                    df = df.drop(df.columns[0], axis='columns')

                df = df.drop(df.columns[7], axis='columns')


                df = df.drop(df[df[0].str.contains(r"REGISTRATION_NUMBER", na=False)==True].index)

                for row in df.values:
                    if row[8] in [r'\N', '']:
                        row[8]= 'Mb'
                    for x in range(len(row)):
                                row[x]=row[x].strip()  
                df, tsn = updateforeign_and_go(df,tsn, 8,'0_y','Sroki_svod.sprav_task_step_name','task_step_name','task_step_id,  task_step_name',['0_y','1_y'],orm_)
                df, dfcategory = updateforeign_and_go(df, dfcategory, 9, 0,'Sroki_svod.sprav_object_category','object_category',"id_object_category, object_category",[0,1],orm_)
                df, dftitle = updateforeign_and_go(df, dftitle, 10, 0,'Sroki_svod.sprav_life_situation_name','life_situation_name',"id_life_situation_name, life_situation_name",[0,1],orm_)
                
                df.insert(10, 'timesosd', dt)



                filestr =   str(Path(name).parent.joinpath("new_file_107key.csv"))
                df.to_csv(filestr, sep=';', quoting = 1, mode='w', header=False, index=False)
                self.mysignal.emit("%s--%s" % (str(50), "Идет загрузка"))    
                orm_.load_local(filestr,"Sroki_svod.a_all_data_107")
                orm_.commit_to()
                Path(filestr).unlink()
                orm_.insert107_to_full107(dt)
                print ("107 с ключами залит успешно")



            
                
                






            elif clicked =="btn_106_fc":
                from load106foreign import give_me_foreign_keys,updateforeign_and_go,addforeign_tsn
                orm_ = Orm()
                dfactions = give_me_foreign_keys("id_actions, actions","Sroki_svod.sprav_actions",orm_)
                dfappael = give_me_foreign_keys("id_appeal_source, appeal_source","Sroki_svod.sprav_appeal",orm_)
                dflsn = give_me_foreign_keys("id_life_situation_name, life_situation_name","Sroki_svod.sprav_life_situation_name",orm_)
                orgtit = give_me_foreign_keys("id_org_title, org_title","Sroki_svod.sprav_org_title",orm_)
                stin=give_me_foreign_keys("task_step_id, task_step_name","Sroki_svod.sprav_task_step_name",orm_)
                login=give_me_foreign_keys("id_login, login","Sroki_svod.sprav_login",orm_)
                
                tsn =  give_me_foreign_keys("task_step_id, task_step_name","Sroki_svod.sprav_task_step_name",orm_)
                name= fileNames 
                for name in fileNames:
                    whatcode = self.encode_Control(name)
                    i=1
                    chunksize=100000
                    filestr =   str(Path(name).parent.joinpath("new_file_.csv"))
                    for chunk in pd.read_csv(name, sep=';', header=None, na_values=r'\N',keep_default_na=False, dtype=str,chunksize=chunksize, engine='python', encoding=whatcode):
                        chunk = chunk.drop(columns=[7,13,14,17,19,20,25])
                        for row in chunk.values:
                           
                            if row[1]=='SENT':
                                row[0]= f"-{row[0]}"
                            if row[17] in ['','-1']:
                                row[17]='35100'
                            if row[3]== r'\N':
                                row[3]= ''
                            for x in [8,9,10,11,13,14,20]:
                                row[x] = self.convertTimeNew(row[x],x)
                            # print(row)
                            for x in range(len(row)):
                                row[x]=row[x].strip()   
                        chunk, dfactions = updateforeign_and_go(chunk,dfactions, 1,'0_y','Sroki_svod.sprav_actions','actions','id_actions, actions',['0_y'],orm_)
                        chunk, dflsn = updateforeign_and_go(chunk,dflsn, 22, 0,'Sroki_svod.sprav_life_situation_name','life_situation_name',"id_life_situation_name, life_situation_name",[0,'1_y'],orm_)
                        chunk, dfappael = updateforeign_and_go(chunk,dfappael, 26, 0,'Sroki_svod.sprav_appeal','appeal_source',"id_appeal_source, appeal_source",[0,1],orm_)
                        chunk,  orgtit = updateforeign_and_go(chunk,orgtit, 15, 0,'Sroki_svod.sprav_org_title','org_title',"id_org_title, org_title",[0,1],orm_)
                        chunk, login = updateforeign_and_go(chunk,login, 8, 0,'Sroki_svod.sprav_login','login',"id_login, login",[0,1],orm_)
                        chunk, tsn = updateforeign_and_go(chunk,tsn, 3, 0,'Sroki_svod.sprav_task_step_name','task_step_name',"task_step_id, task_step_name",[0,1],orm_)
                        # tsn=addforeign_tsn(chunk[[2,3]],tsn, 'Sroki_svod.sprav_task_step_name', "task_step_id, task_step_name",orm_)
                        chunk =chunk.drop(columns=[2,9,10])
                        
                        chunk = chunk.fillna(r'\N')
                        chunk.insert(0, 'st', 3)
                        
                        
                        chunk.to_csv(filestr, sep=';', quoting = 1, mode='a', header=False, index=False)
                        self.mysignal.emit("%s--%s" % (str(i), "Идет обработка файла. 1% - это {} строк. Не отражает реальные %".format(chunksize)) )   
                        i+=1
                    self.mysignal.emit("%s--%s" % ("50", "Загрузка файла на сервер. Не отражает реальные %") )              
                    orm_.load_local(filestr,"Sroki_svod.a_all_data_106")
                    orm_.commit_to()
                    self.mysignal.emit("%s--%s" % ("80", "Удаляю подготовленный файл. Не отражает реальные %") ) 
                    

                   
                    Path(filestr).unlink()
                    # if checkBox106var:
                    #     self.distinctTable('Sroki_svod','a_all_data_106',orm_)
        
        


            orm_.commit_to()
            orm_.connclose()


            if clicked in ['kktnalog','kkttozip']:
               
                self.mysignal.emit("%s--%s" % (str(80), "Процесс займет минут несколько. Ожидаем...") )
                from okved import download_all_origins
                download_all_origins(clicked,calendar, end_date)
                calendar,end_date='',''
            
        except Exception:
            global err
            err=traceback.format_exc()  
            orm_.rollback()
            orm_.connclose()
            
                    
              

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()


