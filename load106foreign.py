from pathlib import Path
from io import BytesIO
import pandas as pd
import numpy as np
from config.orm import Orm

home = Path.home()  
   
def addforeign_tsn(chunko,foreignkeydf,tablename, columnslist, orm_):
    chunklite = chunko.drop_duplicates()
    
    
    # orm_=Orm()
   
   
    for x in chunklite.values:
       
        
        if (len(x[0])>0) and  (foreignkeydf.size==0 or any(foreignkeydf[0]==int(x[0]))==False):
           
            
            y = '"{}","{}"'.format(x[0],x[1])
            print(y)
            
            try:
                orm_.insert_tofc(y,tablename)
                orm_.commit_to()
            except Exception:
                orm_.rollback()
        foreignkeydf = give_me_foreign_keys(columnslist,tablename,orm_)
    # orm_.connclose()
    # 
    # chunktest = foreignkeydf.merge(chunklite,how='left', left_on = [0,1], right_on=[2,3])
    # print (chunktest)    
    return (foreignkeydf)
def updateforeign_and_go(chunk, foreignkeydf, leftcolumn, rightcolumn, tablename,columnnameinsert,columnslist,dropcolist,orm_):
    if foreignkeydf.size>0:
       
        chunktest = chunk.merge(foreignkeydf,how='left', left_on = leftcolumn, right_on=1)
        
        checkchunkforeign = chunktest[leftcolumn].where(chunktest[rightcolumn].isnull()==True, other = None).unique()
        
    else:
        print('попался-попался')
        checkchunkforeign=chunk[leftcolumn].unique()
        print(checkchunkforeign)     
    if len(checkchunkforeign)>0:
        
        
        for x in checkchunkforeign:
            if x:              
                orm_.insertForeign_key(tablename,columnnameinsert, x)
                orm_.commit_to()
            # else:
                # print("Пустое значение ключа {}".format(tablename))
        
        foreignkeydf = give_me_foreign_keys(columnslist,tablename,orm_)
       
        chunk = chunk.merge(foreignkeydf,how='left', left_on = leftcolumn, right_on=1)
        

    else:
        chunk=chunktest
    
    chunk[leftcolumn]=chunk[rightcolumn]
    chunk =chunk.drop(columns=dropcolist)
    return (chunk, foreignkeydf)
def convertTime(t):
        if t in ['', 'NULL']:                                
            # return r"\N"
            return "1900-01-01 00:00:00"
        else:
            t1 = t.split()
            a = t1[0].split('.')
            a[0], a[2] = a[2], a[0]
            t3 = '-'.join(a) + ' ' + t1[1]    
            return t3
def give_me_foreign_keys(columns,tablename,orm_):
   
    x = pd.DataFrame(orm_.randomQuery("Select {} from  {}".format(columns, tablename),1))
    
    return x

# def proof():

#     f = open(home.joinpath('desktop', 'report106.csv'), 'rb')
#     data = f.read()

#     for x in ['cp1251','utf-8']:
#         try:
#             data.decode(x)
#             return x
#         except:
#             print('Ошибка')
#             continue

#     return ''


# for chunk in pd.read_csv(home.joinpath('desktop', 'report106.csv'), sep=';', header=None, na_values='NULL',keep_default_na=False, dtype=str,chunksize=10000, engine='python', encoding=proof()):
#     chunk = chunk.drop(columns=[7,13,14,17,19,20,25])
#     for row in chunk.values:
#         if row[1]=='SENT':
#             row[0]= f"-{row[0]}"
#         if row[17] in ['','-1']:
#             row[17]='35100'
#         for x in [8,9,10,11,13,14,20]:
#             row[x] = convertTime(row[x])