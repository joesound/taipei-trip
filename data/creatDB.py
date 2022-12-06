import mysql.connector
from utils.config import MYSQL_ACCOUNT, MYSQL_PASSWORD
SHOW_DATABSES = "SHOW DATABASES"
SELECT_TABLES = "SELECT TABLES"


mydb = mysql.connector.connect(
  host="localhost",
  user = MYSQL_ACCOUNT,
  password = MYSQL_PASSWORD,
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS `taipei_attraction`")
mycursor.execute("USE taipei_attraction")
mycursor.close()
