# backend/database/db.py
import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",  # Change this to your MySQL password
        database="procad"
    )
