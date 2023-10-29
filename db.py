import configparser
from mysql.connector import Error, MySQLConnection
from typing import Optional

def connectDB() -> Optional[MySQLConnection]:
    parser = configparser.ConfigParser()
    parser.read('config.ini')
    db = {}
    if parser.has_section('mysql'):
        items = parser.items('mysql')
        for item in items:
            db[item[0]] = item[1]
    else:
        print('No MySQL section in config.ini file')
        return None
    
    try:
        conn = MySQLConnection(**db)
        if conn.is_connected():
            print('Connected Safely!!')
            return conn
        else:
            print('Connection Failed')
    except Error as e:
        print(e)
    
    return None
