import sqlite3
from sqlite3 import Error

# Класс работы с БД
class dbase():
# ---------------------------------
#   Инициализатор
    def __init__(self,pair):

        self.db_name = pair+".db"
#       соединение с БД
        self.connection = None
        try:
            self.connection = sqlite3.connect(self.db_name)
            self.cursor = self.connection.cursor()
#            print("Connection to SQLite DB successful")
        except Error as e:
            print(f"The error '{e}' occurred")

#       создание таблиц
        self.min_table()
        self.hour_table()
        self.day_table()
        self.level_table()
#        self.sketchChart_table()

        return

# ---------------------------------
#   Метод завершения изменений
    def commit(self):

        self.connection.commit()
        self.connection.close()

        return

# ---------------------------------
#   Метод записи данных в таблицу mins
    def msave(self, data):

        record = [None,data['low'],data['high'],data['open'],data['close'],
                  data['year'],data['month'],data['day'],data['hour'],data['min'],data['volume']]
        self.cursor.execute(''' INSERT INTO mins VALUES(?,?,?,?,?,?,?,?,?,?,?) ''',record)

        return

# ---------------------------------
#   Метод записи данных в таблицу hours
    def hsave(self, data):

        record = [None,data['low'],data['high'],data['open'],data['close'],
                  data['year'],data['month'],data['day'],data['hour'],data['volume']]
        self.cursor.execute(''' INSERT INTO hours VALUES(?,?,?,?,?,?,?,?,?,?) ''',record)

        return

# ---------------------------------
#   Метод записи данных в таблицу days
    def dsave(self, data):

        record = [None,data['low'],data['high'],data['open'],data['close'],
                  data['year'],data['month'],data['day'],data['volume']]
        self.cursor.execute(''' INSERT INTO days VALUES(?,?,?,?,?,?,?,?,?) ''',record)

        return

# ---------------------------------
#   Метод записи данных в таблицу days
    def levsave(self, data):

        record = [None,data['timeframe'],data['level'],data['plus'],data['minus']]
        self.cursor.execute(''' INSERT INTO levels VALUES(?,?,?,?,?) ''',record)
        self.connection.commit()
        
        return

# ---------------------------------
#   Метод очистки таблицы
    def clear(self,table,cond):

        query = "DELETE FROM " + table
        if(len(cond) > 0):
            query += " WHERE "+cond
        self.cursor.execute(query)
        self.connection.commit()

        return

# ---------------------------------
#   Метод выборки данных из БД дней
    def days_select(self, where):

        query = "SELECT * FROM days WHERE " + where + " ORDER BY month,day"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()

        return rows

# ---------------------------------
#   Метод выборки данных из БД дней
    def hours_select(self, where):

        query = "SELECT * FROM hours WHERE " + where + " ORDER BY day,hour"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()

        return rows

# ---------------------------------
#   Метод выборки данных из БД дней
    def mins_select(self, where):

        query = "SELECT * FROM mins WHERE " + where + " ORDER BY day,hour,mint"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()

        return rows

# ---------------------------------
#   Метод создания таблицы или индекса
    def create_table(self,create_table_sql):

        try:
            c = self.connection.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)
            
        return
    
# ---------------------------------
#   Метод задания структуры таблицы учета минут
    def min_table(self):

        sql_create_mins_table = """
                CREATE TABLE IF NOT EXISTS mins (
                id integer PRIMARY KEY,
                low float,
                high float,
                open float,
                close float,
                year unsigned integer,
                month unsigned integer,
                day unsigned integer,
                hour unsigned integer,
                mint unsigned integer,
                volume unsigned integer); """
        self.create_table(sql_create_mins_table)

        sql_create_mins_table = """
                CREATE INDEX IF NOT EXISTS imins ON mins (day, hour, mint); """
        self.create_table(sql_create_mins_table)

        return

# ---------------------------------
#   Метод задания структуры таблицы учета часов
    def hour_table(self):
    
        sql_create_hours_table = """
                CREATE TABLE IF NOT EXISTS hours (
                id integer PRIMARY KEY,
                low float,
                high float,
                open float,
                close float,
                year unsigned integer,
                month unsigned integer,
                day unsigned integer,
                hour unsigned integer,
                volume unsigned integer ); """
        self.create_table(sql_create_hours_table)

        sql_create_hours_table = """
                CREATE INDEX IF NOT EXISTS ihours ON hours (day, hour); """
        self.create_table(sql_create_hours_table)
        
        return

# ---------------------------------
#   Метод задания структуры таблицы учета дней
    def day_table(self):

        sql_create_days_table = """
                CREATE TABLE IF NOT EXISTS days (
                id integer PRIMARY KEY,
                low float,
                high float,
                open float,
                close float,
                year unsigned integer,
                month unsigned integer,
                day unsigned integer,
                volume unsigned integer ); """
        self.create_table(sql_create_days_table)

        sql_create_days_table = """
                CREATE INDEX IF NOT EXISTS idays ON days (day); """
        self.create_table(sql_create_days_table)

        return

# ---------------------------------
#   Метод задания структуры таблицы учета уровней
#   pair - валютная пара
#   timeframe - образующий таймфрейм
#   level - средний уровень
#   plus - возможное отклонение уровня вверх
#   minus - возможное отклонение уровня вниз
    def level_table(self):

        sql_create_levels_table = """
                CREATE TABLE IF NOT EXISTS levels (
                id integer PRIMARY KEY,
                timeframe character,
                level float,
                plus float,
                minus float); """
        self.create_table(sql_create_levels_table)

        sql_create_levels_table = """
                CREATE INDEX IF NOT EXISTS ilevels ON levels (timeframe); """
        self.create_table(sql_create_levels_table)
        
        return
    
# ---------------------------------
#   Установка символов в зависимости от соотношения со средним размером свечи
#       0-5% - 4             0-5% - 4
#       5-50% вверх - 5      5-50% вниз - 3
#       50-150% вверх - 6    50-150% вниз - 2
#       >150% вверх - 7      >150% вниз - 1
#       >300% вверх - 8      >300% вниз - 0
#   Метод задания структуры таблицы упрощенных графиков
#   pair - валютная пара
#   timeframe - образующий таймфрейм
#   number - номер участка цепи свечей (0, ...), это значит, что цепь может быть
#            разбита на части для хранения в таблице
#   bodyChain - цепочка символов-характеристик тела свечи
#   upshadow - цепочка символов-характеристик верхней тени свечи
#   downshadow - цепочка символов-характеристик нижней тени свечи
    def sketchChart_table(self):

        sql_create_sketchChart_table = """
                CREATE TABLE IF NOT EXISTS sCharts (
                id integer PRIMARY KEY,
                pair character,
                timeframe character,
                number int,
                bodyChain varchar,
                upshadow varchar,
                downshadow varchar
                ); """
        self.create_table(sql_create_sketchChart_table)

        sql_create_sketchChart_table = """
                CREATE INDEX IF NOT EXISTS isCharts ON sCharts (pair,timeframe); """
        self.create_table(sql_create_sketchChart_table)

        return