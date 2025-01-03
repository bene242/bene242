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

def create_data(conn):    
    cursor = conn.cursor()
    print('inserting data...')
    for i in range(1,6):
        insert_sql = ("INSERT INTO product "
                   "(name, stock, price, created) "
                   "VALUES(?, ?, ?, ?)")

        params = ("product " + str(i), 3+i*4,
                        0.4+i*8, datetime.now())
        cursor.execute(insert_sql, params)
        product_id = cursor.lastrowid
        print('inserted with id=', product_id)

    conn.commit()
    cursor.close()
    print('done')

# open data
conn = open_database()

# creating table demo
#create_table(conn)
create_data(conn)

# close data
conn.close()