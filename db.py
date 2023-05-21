import configparser
# import mysql.connector
from mysql.connector import Error, MySQLConnection

def connectDB():
    parser = configparser.ConfigParser()
    parser.read('config.ini')
    db = {}
    if parser.has_section('mysql'):
        items = parser.items('mysql')
        for item in items:
            db[item[0]] = item[1]
    else:
        print('No MySQL section in config.ini file')
        return 0
    conn = None
    try:
        conn = MySQLConnection(**db)
        if conn.is_connected():
            print('Connected Safely!!')
        else:
            print('Connection Failed')
        return conn
    except Error as e:
        print(e)
        return 0
    # finally:
    #     if conn is not None and conn.is_connected():
    #         conn.close()
    #         print('Connection closed.')

