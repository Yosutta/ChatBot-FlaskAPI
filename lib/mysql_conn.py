import mysql.connector

mysqldb = mysql.connector.connect(
    # host="https://sv82.ifastnet.com/cpsess4172857946/3rdparty/phpMyAdmin",
    # host="185.27.133.16",
    host="www.sv82.ifastnet.com",
    user="mevivubi_mevivu",
    password="@mevivucom@123",
    database="mevivubi_thinh01165"
)

mysqlerror = mysql.connector.Error

if (mysqldb.is_connected()):
    print("Connected to MySQL Database")
else:
    print("MySQL Database not connected")
