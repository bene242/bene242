import sqlite3
from datetime import datetime
from prettytable import PrettyTable


def open_database():    
    db = 'pydb.db' 

    print('Connecting to SQLite...')
    conn = sqlite3.connect(db)
    print('connected')  

    return conn

def create_table(conn):
    cursor = conn.cursor()
    sql = ''' create table if not exists product(
        id integer primary key autoincrement,
        name char(30) not null,
        stock integer,
        price float,
        created datetime
    )'''

    cursor.execute(sql)
    conn.commit() 
    print('created a table')

# open data
conn = open_database()

# creating table demo
create_table(conn)

# close data
conn.close()