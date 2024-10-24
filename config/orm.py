import mysql.connector
from mysql.connector import Error
from datetime import datetime


class Orm():
    """ Осуществляет подключение к базе данных. Описывает методы, которые
    используются для создания объекта. Описание объектов в самих методах """
    
    def __init__(self):
        # self.set_connect = ("10.252.44.38", "root", "P@ssw0rd", "Sroki_svod")
        self.set_connect = ("localhost", "root", "", "Sroki_svod")
        self.connection = self.create_connection(*self.set_connect)
        # 10.252.44.38 P@ssw0rd


    def create_connection(self, host_name, user_name, user_password, db_name):
        """ Создает подключение и возвращает его """

        connection = None

        try:
            connection = mysql.connector.connect(
                host=host_name,
                user=user_name,
                passwd=user_password,
                database=db_name,
                allow_local_infile=True
            )
            print("Connection to MySQL DB successful")

        except Error as e:
            print(f"--------------------ОШИБКА---------------- '{e}' ")

        return connection


    def take_actual_date(self, table):
        """ Забирает даты, которые присутствуют в выбранной таблице. 
        Возвращает их в виде списка """

        query = """
        SELECT DISTINCT datelikedale 
        FROM %s
        ORDER BY datelikedale DESC
        LIMIT 30
        """ % table

        cursor = self.connection.cursor()

        try:
            cursor.execute(query)
            rows = cursor.fetchall()
            result = [0]*len(rows)
            for i in range(0, len(rows)):
                result[i] = rows[i][0].strftime('%d.%m.%Y')
            return result

        except Error as e:
            print(f"The error '{e}' occurred")

    
    

    def create_list(self, el, length, index):
        """ Создает список определенной длины, вставляя элемент в нужное место списка.
        Возвращает созданный список """
        arr = [0]*(length-1)
        arr.insert(index, el)
        return arr


    def pull(self, ch_list: list, pull_list: list, index: int):
        """ Вставляет значения из списка в соответствующее индексу место двумерного списка """

        for i in range(len(pull_list)):
            ch_list[i][index] = pull_list[i]

    def load_local(self, val,tablename):
        #101
        cursor = self.connection.cursor()
        sql ='SET sql_mode = "";'
        cursor.execute(sql)
        sql ='LOAD DATA LOCAL INFILE "'+ val.replace('\\', '/')+'" REPLACE INTO TABLE '+ tablename +'  CHARACTER SET utf8 FIELDS TERMINATED BY ";"  ENCLOSED BY """" LINES TERMINATED BY "\r\n" ;'
        cursor.execute(sql)
        #  (history_id, actions, task_step_id, task_step_name, card_id, card_task_id, tax_code, login, start_ts,end_ts , start_ts_reg, end_ts_reg , org_title, out_date, in_date, registration_number, life_situation_name, snts_code, dubl,  appeal_source, date_reg_appeal)

    def insert_to(self, val,tablename):
        cursor = self.connection.cursor()
        sql = "REPLACE INTO " + tablename + " VALUES %s" % val
        cursor.execute(sql)
    def insert107_to_full107(self, datesosd):
        cursor = self.connection.cursor()
        # sql = "INSERT INTO 107_gen_ci.full_all_data_107 Select *, '%s' from 107_gen_ci.all_data_107" % datesosd
        # cursor.execute(sql)
        sql = "INSERT INTO Sroki_svod.info107 VALUES ('%s', '%s')" %(datesosd, datesosd[:10])
        cursor.execute(sql)
    
    def commit_to(self):
        try:
            self.connection.commit()
        except  Exception:
            self.connection.rollback()
    def connclose(self):
        
        self.connection.close()
        print("Соединение закрыто")
    def rollback(self):
        self.connection.rollback()


    def SelectFromTableToXl(self, tablename, start, end):
        cursor = self.connection.cursor()
        if tablename !='kkt':
            sql = "SELECT * FROM %s WHERE datelikeDale >= '%s' AND datelikeDale <= '%s' order by datelikedale, id_region" % (tablename, start, end)
        else:
            sql="SELECT datelikedale, CAST(id_region As UNSIGNED) As id_region, count_NP, count_KKT, vir_value FROM kkt WHERE datelikeDale >= '%s' AND datelikeDale <= '%s' order by datelikedale, id_region" % (start, end)
        cursor.execute(sql)
        return cursor.fetchall()
    def SelectFromTable_Names(self,tablename):
        cursor = self.connection.cursor()
        sql = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME= '%s'" % (tablename)
        cursor.execute(sql)
        return cursor.fetchall()
    def trunc (self, basename, tablename):
        cursor = self.connection.cursor()
        sql = "TRUNCATE " + basename +"." + tablename + ""
        cursor.execute(sql)
    def delfrom107(self,datesosd):
        cursor = self.connection.cursor()
        sql = "DELETE FROM Sroki_svod.a_all_data_107 WHERE time_sosd='%s'" % (datesosd)
        cursor.execute(sql) 
        sql = "DELETE FROM Sroki_svod.info107 WHERE time_sosd='%s'" % (datesosd)
        cursor.execute(sql) 

    def runproc(self,btn):
        cursor = self.connection.cursor()
        # sql = "CALL Sroki_svod.%s()" % btn
        cursor.callproc(btn)

    def select_date_for_107(self,cal_date,btnName):
        cursor = self.connection.cursor()
        if btnName:
            sql = "SELECT MAX(time_sosd) FROM Sroki_svod.info107"
            cursor.execute(sql)
            return cursor.fetchone()
        else:    
            sql = "SELECT time_sosd FROM Sroki_svod.info107 WHERE time_sosd>= '%s 00:00:00'  AND time_sosd<= '%s 23:59:59' ORDER BY time_sosd ASC" %(cal_date, cal_date)
            cursor.execute(sql)
            return cursor.fetchall()

    def countTable(self,baseTableName):
        cursor = self.connection.cursor()
        sql = "SELECT COUNT(*) FROM %s" %(baseTableName)
        cursor.execute(sql)
        return cursor.fetchone()
    # def test_name(self):


    # имена колонок в таблице бд
        # names = cursor.column_names
        # print(names)
    def randomQuery(self,query, retbool):
        cursor = self.connection.cursor()
        cursor.execute('%s' %query)
        if retbool:
            return cursor.fetchall()
        else:
            return cursor.fetchone()
    
    # `TABLES` - 38
    def infodump(self, time4asc, allt):
       
        if allt:
            info = self.randomQuery("SELECT TABLE_SCHEMA, TABLE_NAME, UPDATE_TIME FROM information_schema.`TABLES` WHERE TABLES.TABLE_SCHEMA NOT IN ('mysql','information_schema','performance_schema','sys','wordpress', 'Pril4_LKFL') AND ENGINE IS NOT NULL AND ENGINE<>'CSV' ORDER BY TABLE_SCHEMA ASC",1)
        else:   
            info = self.randomQuery("SELECT TABLE_SCHEMA, TABLE_NAME, UPDATE_TIME FROM information_schema.`TABLES` WHERE TABLES.TABLE_SCHEMA NOT IN ('mysql','information_schema','performance_schema','sys','wordpress','Pril4_LKFL') AND ENGINE IS NOT NULL AND ENGINE<>'CSV' AND UPDATE_TIME IS NOT NULL AND UPDATE_TIME >='%s' ORDER BY TABLE_SCHEMA ASC" %time4asc,1)
        return (info)
    def insert_tokkt(self,val,tablename):
        cursor=self.connection.cursor()
        sql='REPLACE INTO %s VALUES %s' %(tablename,val)
        cursor.execute(sql)

    def insertForeign_key(self,tablename, column_name, val):
        cursor=self.connection.cursor()
        sql='REPLACE INTO {} SET {} = "{}"'.format(tablename, column_name, val)
        cursor.execute(sql)
    
    def inserttimekey(self,tablename, column_name, val):
        cursor=self.connection.cursor()
        sql='UPDATE {} SET {} = "{}"'.format(tablename, column_name, val)
        cursor.execute(sql)
    def insert_tofc(self,val,tablename):
        cursor=self.connection.cursor()
        sql='REPLACE INTO %s VALUES (%s)' %(tablename,val)
        cursor.execute(sql)