## IMPORTS ##
from dotenv import load_dotenv
import mysql.connector
import os
import json

## INIT ##
# Loading environment variables
load_dotenv()
MYSQL_USER = os.getenv('MYSQL_USER')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
# Initializing the db
cnx = mysql.connector.connect(
    host="localhost",
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
    database='password_list'
)
cursor = cnx.cursor(buffered=True)


def main():
    print("Please choose the appropriate option.")
    print("1. Returning user.\n2. New user.")
    choice = input()
    if choice == "1":
        login()
    elif choice == "2":
        signup()


def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    queryU = "SELECT UserName FROM UserList WHERE UserName = %s"
    queryP = "SELECT Password FROM UserList WHERE Password = %s"
    cursor.execute(queryU, (username,))
    if cursor.rowcount == 0:
        print(
            "The username doesnt exist!! Try signing up or entering the correct username.")
        login()
    else:
        pass


def signup():
    username = input("Enter your username: ")
    password = input("Enter a strong password: ")
    queryC = "SELECT UserName FROM UserList WHERE UserName = %s"
    query = "INSERT INTO UserList (UserName, Password) VALUES (%s, %s)"
    cursor.execute(queryC, (username,))
    if cursor.rowcount == 0:
        cursor.execute(query, (username, password))
        cnx.commit()
    else:
        print("Username already exists, Enter another username.")
        signup()


if __name__ == "__main__":
    main()
