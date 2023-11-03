

# pip install mysql-connector-python 
# pip install pymysql
# pip install mysqlclient
import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user= 'root',
    passwd= '112233'

)

# prepare a cursor object
cursorobject = database.cursor()

# create a database
cursorobject.execute('CREATE DATABASE elderco')


print('All Done!')