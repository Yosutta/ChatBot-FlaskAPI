import mysql.connector

mysqldb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="chatbot_flask"
)
