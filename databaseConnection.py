from flask import Flask, request
import mysql.connector

# Configure MySQL connection
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='testing'
)

cursor = db.cursor()

def createUser(name,email,password):
    result = cursor.execute("""
        INSERT INTO `USERS`(`id`,`name`,`email`,`password`) VALUES (NULL,'{}','{}','{}')
    """.format(name,email,password)
    )
    db.commit()
    if result is None:
        return True
    else:
        return False
def createjob(title,description,location,salary):
    result = cursor.execute("""
        INSERT INTO `post`(`id`,`title`,`jdescription`,`location`,`salary`) VALUES (NULL,'{}','{}','{}','{}')
    """.format(title,description,location,salary)
    )
    db.commit()
    if result is not None:
        return False
    else:
        return True

def loginUser(email,password):
    cursor.execute("""
        SELECT * FROM USERS WHERE email LIKE '{}' and `password` like '{}'""".format(email,password)
    )
    users = cursor.fetchall()
    if len(users)>0:
        return users
    else:
        return None

def loginAdmin(email,password):
    cursor.execute("""
        SELECT * FROM ADMINS WHERE email LIKE '{}' and `password` like '{}'""".format(email,password)
    )
    users = cursor.fetchall()
    if len(users)>0:
        return users
    else:
        return None



