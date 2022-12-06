import mysql.connector
# from config import SQL_USER, SQL_PASSWORD
from utils.config import MYSQL_ACCOUNT, MYSQL_PASSWORD
#資料庫連線
mydb = mysql.connector.connect(     #登入資料庫
                host="localhost",
                user= MYSQL_ACCOUNT,
                password= MYSQL_PASSWORD,
                database="taipei_attraction"
                )

#建立資料表 function 
def creat_table(table_style):
    mycursor = mydb.cursor()
    sql = "CREATE TABLE IF NOT EXISTS `taipei_attraction`." + table_style
    print(sql)
    mycursor.execute(sql)
    mycursor.close()

#資料表style

#建立use table(id, name, email)
order_style = "`order`(`id` bigint PRIMARY KEY AUTO_INCREMENT,`number` bigint NOT NULL, `price` bigint NOT NULL, `attractionid` bigint NOT NULL,`attractionname` varchar(255) NOT NULL, `address` varchar(255) NOT NULL,`image_url` varchar(255) NOT NULL, `date` DATE NOT NULL  ,`time` varchar(255) NOT NULL, `username` varchar(255) NOT NULL, `email` varchar(3000) NOT NULL, `phone` bigint NOT NULL, `status` INT NOT NULL)"

creat_table(order_style)

