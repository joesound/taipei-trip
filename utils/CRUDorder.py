import mysql.connector
from utils.config import MYSQL_ACCOUNT, MYSQL_PASSWORD
account = MYSQL_ACCOUNT()
password = MYSQL_PASSWORD()
mydb = mysql.connector.connect(     #登入資料庫
                host="localhost",
                user= account ,
                password= password,
                database="taipei_attraction"
                )


def creat_order(order_info):
    getNumber = order_info["number"]
    getPrice = order_info["order"]["price"]
    getAttid = order_info["order"]["trip"]["attraction"]["id"]
    getAttname = order_info["order"]["trip"]["attraction"]["name"]
    getAdress =  order_info["order"]["trip"]["attraction"]["address"]
    getImage =  order_info["order"]["trip"]["attraction"]["image"]
    getDate =  order_info["order"]["trip"]["date"]
    getTime =  order_info["order"]["trip"]["time"]
    getUname = order_info["order"]["contact"]["name"]
    getEmail = order_info["order"]["contact"]["email"]
    getPhone = order_info["order"]["contact"]["phone"]
    getStatus = order_info["status"]

    mycursor = mydb.cursor()
    try:
        crete_order_sql = "INSERT INTO `order` (number, price, attractionid, attractionname, address, image_url, date, time, username, email, phone, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
        # delete_booking_sql = "DELETE FROM booking WHERE email=%s;"
        instruction = crete_order_sql
        val=(getNumber, getPrice, getAttid, getAttname, getAdress, getImage, getDate, getTime, getUname, getEmail, getPhone, getStatus, )
        mycursor.execute(instruction.lower(), val)
        mydb.commit()
        mycursor.close  
        data = {
            "data":{
                "number":getNumber,
                "payment":{
                    "status":getStatus,
                    "message":"付款成功"
            }
        }}
        return 200, data
    except mysql.connector.Error as err:
        print(err)
        mycursor.close
        return 500, {"message":err}


def read_order(email):
    mycursor = mydb.cursor()

    try:
        get_order_info = "SELECT * FROM order WHERE email=%s ORDER BY date ASC"
        val = (email, )
        mycursor.execute(get_order_info.lower(), val)
        user_order_info = mycursor.fetchone()
        # if len(datas) > 5:
        #         data = {
        #             "nextPage": page+1,
        #             "data":[]
                    
        #         }
        #         datas = datas[0:12]
        # elif len(datas) < 5 and len(datas)>0:
        #     data = {
        #         "nextPage": None,
        #         "data":[]
        #     }
        # else:
        #     data = {
        #         "nextPage": None,
        #         "data":[]
        #     }
        #     return data

        # for each_data in user_order_info:
        #     insert_data = {
        #         "id": each_data[0],
        #         "name": each_data[1],
        #         "category": each_data[2],
        #         "description": each_data[3],
        #         "address": each_data[4],
        #         "transport": each_data[5],
        #         "mrt": each_data[6],
        #         "latitude": each_data[7],
        #         "longitude": each_data[8],
        #         "images": [each_data[9].split(",")]
        #     }
        #     data["data"].append(insert_data)
        mycursor.close  
        return 200, user_order_info
    except mysql.connector.Error as err:
        mycursor.close
        return 500, {"message":err}
    

def read_order_by_number(number):
    mycursor = mydb.cursor()

    try:
        get_order_info = "SELECT * FROM `order` WHERE number=%s"
        val = (number, )
        mycursor.execute(get_order_info.lower(), val)
        user_order_info = mycursor.fetchone()
        mycursor.close  
        data = {
            "data":{
                "number": user_order_info[1],
                "price": user_order_info[2],
                "trip":{
                    "attraction":{
                        "id":user_order_info[3],
                        "name":user_order_info[4],
                        "address":user_order_info[5],
                        "image":user_order_info[6],
                    },
                "date":str(user_order_info[7]),
                "time":user_order_info[8],
                },
                "contact":{
                    "name":user_order_info[9],
                    "email":user_order_info[10],
                    "phone":user_order_info[11],
                },
                "status":user_order_info[12],
            }
        }
        return 200, data
    except mysql.connector.Error as err:
        mycursor.close
        return 500, {"message":err}




# order_info = {
#     "prime":"1234567890",
#     "price":"2500",
#     "attractionid":2,
#     "attractionname":"平安鐘",
#     "adress":"新北市",
#     "image_url":"fdskgpkdpf;gkdpfkgdf",
#     "date":'2022-04-06',
#     "time":"afternoon",
#     "username":"qq",
#     "email":"123@g",
#     "phone":222223333
# }

# data = creat_order(order_info)
# print(data)