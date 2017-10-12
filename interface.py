import login
import createquiz
import takequiz
import MySQLdb
import os
import Tkinter

db = MySQLdb.connect("localhost", "root", "seecs@123", "quiz_system")
cursor = db.cursor()
db.autocommit(True)

if __name__=="__main__":

    if (login.main(cursor)=="instructor"):
        createquiz.main(cursor)
    else:
        takequiz.main(cursor)
    cursor.close()


