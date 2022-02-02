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
    pass


def signup():
    pass
