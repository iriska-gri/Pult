import numpy as np
import pandas as pd
from datetime import datetime, timedelta, date
import datetime
from config.orm import Orm
from pathlib import Path
import math
# def convertTimeNew(t):
#     t1 = t.split(' +')
#     tdate = datetime.strptime(t1[0], '%d.%m.%Y %H:%M:%S')
#     hours, minutes = map(int, t1[1].split(':'))
    
     
    
#     return (tdate-timedelta(hours=(hours-3),minutes=minutes)) 



# t = "05.11.2020 09:28:04 +07:00"
# a= convertTimeNew(t)
# print(a)
def encode_Control(filename):
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

# fileNames= r'C:\Users\kuroe\Desktop\projects\1400.csv'

# orm_ = Orm()
# dfcategory = give_me_foreign_keys("id_object_category, object_category","Sroki_svod.sprav_object_category",orm_)

# dftitle = give_me_foreign_keys("id_life_situation_name, life_situation_name","Sroki_svod.sprav_life_situation_name",orm_)
# tsn =  give_me_foreign_keys("task_step_id, task_step_name","Sroki_svod.sprav_task_step_name",orm_)
# name= fileNames 
# if Path(name).suffix != '.csv':
#     df = pd.read_excel(name,dtype=str,na_values=r'\N',keep_default_na=False)
# else:
#     # self.mysignal.emit("%s--%s" % (str(1), "Открываю файлик и смотрю что там за кодировочка..."))
#     whatcode = encode_Control(name)
#     df = pd.read_csv(name, sep=';',na_values=r'\N',keep_default_na=False,encoding=whatcode,dtype=str,header=None,)
    
# if len(df.columns)>11: 
# # or df.columns[0]!='REGISTRATION_NUMBER':
#     df = df.drop(df.columns[0], axis='columns')

# df = df.drop(df.columns[7], axis='columns')


# df = df.drop(df[df[0].str.contains(r"REGISTRATION_NUMBER", na=False)==True].index)

# for row in df.values:
#      if row[8] in [r'\N', '']:
#         row[8]= 'Mb'

# df, tsn = updateforeign_and_go(df,tsn, 8,'0_y','Sroki_svod.sprav_task_step_name','task_step_name','task_step_id,  task_step_name',['0_y','1_y'],orm_)
# df, dfcategory = updateforeign_and_go(df, dfcategory, 9, 0,'Sroki_svod.sprav_object_category','object_category',"id_object_category, object_category",[0,1],orm_)
# df, dftitle = updateforeign_and_go(df, dftitle, 10, 0,'Sroki_svod.sprav_life_situation_name','life_situation_name',"id_life_situation_name, life_situation_name",[0,1],orm_)
# df.insert(10, 'st', 3)
# print (df)
orm_  = Orm()
fileNames= r'C:\Users\kuroe\Desktop\projects\25.csv'
# from load106foreign import give_me_foreign_keys,updateforeign_and_go,addforeign_tsn
# dfstatus = give_me_foreign_keys("id_status_obrabotki, status_obrabotki","Sroki_svod.sprav_ais_status_obrabotki",orm_)
# dfpriznak = give_me_foreign_keys("id_prisnak_statusa_obrabotki, prisnak_statusa_obrabotki","Sroki_svod.sprav_ais_prisnak_statusa_obrabotki",orm_)
# dfSooNstat =  give_me_foreign_keys("id_status_v_SOON, status_v_SOON","Sroki_svod.sprav_ais_status_v_SOON",orm_)
# df = pd.read_excel(fileNames,header=None, dtype=str, na_values='NULL',keep_default_na=False, skiprows=1) #номер листа с 0
# df = df.drop(columns=[0,1,2,4,5,7,12,13,14], axis=1)
# df[16]=4
# df, dfstatus = updateforeign_and_go(df,dfstatus, 9,0,'Sroki_svod.sprav_ais_status_obrabotki','status_obrabotki','id_status_obrabotki, status_obrabotki',[0,1],orm_)
# df, dfpriznak = updateforeign_and_go(df, dfpriznak, 10, 0,'Sroki_svod.sprav_ais_prisnak_statusa_obrabotki','prisnak_statusa_obrabotki',"id_prisnak_statusa_obrabotki, prisnak_statusa_obrabotki",[0,1],orm_)
# df, dfSooNstat = updateforeign_and_go(df, dfSooNstat, 11, 0,'Sroki_svod.sprav_ais_status_v_SOON','status_v_SOON',"id_status_v_SOON, status_v_SOON",[0,1],orm_)
# print(df)

