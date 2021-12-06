import mysql.connector

if __name__ == '__main__':
    mydb = mysql.connector.connect(host="localhost", user="root", password="Abest4ever@", database="burgerdb")
    curr = mydb.cursor()
    # print(mydb)
    # curr.execute("CREATE DATABASE burgerdb")
    # curr.execute("SHOW DATABASES")
    # for db in curr:
    #     print(db)

