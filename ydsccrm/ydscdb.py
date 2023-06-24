#Install Mysql on your computer
#https://dev.mysql.com/downloads/installer
#pip install
#pip install mysql-connector
#pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'root'
)

#Prepare a cursor object
cursorObject = dataBase.cursor()

#Create Database
cursorObject.execute("CREATE DATABASE ydscdb")
print('All Done!!')
