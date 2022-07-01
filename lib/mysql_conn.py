import mysql.connector

# mysqldb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="password",
#     database="chatbot_flask"
# )

mysqlerror = mysql.connector.Error

mysqldb = mysql.connector.connect(
    host="sql6.freesqldatabase.com",
    user="sql6503307",
    password="QliwI7kMEg",
    database="sql6503307",
    port="3306"
)

if (mysqldb.is_connected()):
    print("Connected")
else:
    print("Not connected")
