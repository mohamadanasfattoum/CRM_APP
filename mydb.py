from project.secrets import DATABASE_PASSWORD

# pip install mysql-connector-python 
# pip install pymysql
# pip install mysqlclient
import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user= 'root',
    passwd= DATABASE_PASSWORD

)

# prepare a cursor object
cursorobject = database.cursor()

# create a database
cursorobject.execute('CREATE DATABASE crm_db')


print('All Done!')