def welcome():
    print "____________________________________________________"
    print "WELCOME TO THE QUIZ APPLICATION"
    print "____________________________________________________"
    print "Please enter your credentials:"

def verify(username, password, cursor):
    while True:

        sql = "SELECT id_type from login where login.username='%s' AND login.password='%s'"
        cursor.execute(sql % (username, password))
        result=cursor.fetchone()

        if (result):
            return True, result[0]
        else:
            print "THIS ID DOESN'T EXIST IN DATABASE"
            print "PLEASE ENTER THE CORRECT CREDENTIALS"
            return False, None

def input():
    username = raw_input("USERNAME: ")
    password = raw_input("PASSWORD: ")
    return username, password

def main(cursor):
    welcome()
    while True:
        username, password = input()
        result, id_type = verify(username, password, cursor)
        if (result):
            break
    return id_type







