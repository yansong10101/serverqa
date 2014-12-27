from django.test import TestCase
import MySQLdb

# Create your tests here.
def db_read():
    connection = MySQLdb.connect(host='127.0.0.1', user='root', passwd='yansong', db='mydatabase')
    cursor = connection.cursor()
    cursor.execute('select user_name from test')
    data = cursor.fetchall()
    str = ''
    for row in data:
        str += row[0]
    cursor.close()
    connection.close()
    return str