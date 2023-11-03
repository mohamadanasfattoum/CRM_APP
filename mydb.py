import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user= 'root',
    passwd= '112233'

)

# prepare a cursor object
cursorObject = dataBase.cursor()

# create a database
cursorObject.execute('CREATE DATABASE elderco')


print('All Done!')