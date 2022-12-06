import datetime
import requests
from utils.config import TRADE_KEY, PARTNER_KEY
import json
parner_key = PARTNER_KEY()

def trade_order(trade_info):
    trade_status = False
    order_number = datetime.datetime.now().strftime('%Y%m%d%H%M')

    url = "https://sandbox.tappaysdk.com/tpc/payment/pay-by-prime"
    headers = {
        'content-type': 'application/json',
        "x-api-key": parner_key
    }
    data = {
        "prime": trade_info["prime"],
        "partner_key": parner_key,
        "merchant_id": "wltaipeitrip_CTBC",
        "details":"TapPay Test",
        "order_number":order_number,
        "amount": 100,
        "cardholder": {
            "phone_number": trade_info["phone"],
            "name": trade_info["user_name"],
            "email": trade_info["email"],
        },
        "remember": True
    }
    resp = requests.post(url, headers=headers ,data = json.dumps(data))
    resp_data = resp.json()
    if resp_data["status"]==0:
        trade_status = True
        return [trade_status, order_number]
    
    else:
        return [trade_status, resp_data["msg"]]






























    # getPrime = order_info["prime"]
    # getPrice = order_info["price"]
    # getAttid = order_info["attractionid"]
    # getAttname = order_info["attractionname"]
    # getAdress =  order_info["adress"]
    # getImage =  order_info["image_url"]
    # getDate =  order_info["date"]
    # getTime =  order_info["time"]
    # getUname = order_info["username"]
    # getEmail = order_info["email"]
    # getPhone = order_info["phone"]
    
    