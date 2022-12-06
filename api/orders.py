from flask import Flask, render_template, request, session, redirect, url_for, Blueprint, make_response
import json
from utils.creatJWT import creat_user_JWT, decode_user_JWT
from utils.ordercheck import trade_order
from utils.CRUDorder import read_order, creat_order, read_order_by_number
from utils.CRUDbook import delete_booking
from utils.config import URL_BS

request_url = URL_BS()

app_api_order = Blueprint('uesr_order', __name__, url_prefix='/api')

@app_api_order.route("/orders", methods=['GET','POST','DELETE','OPTIONS'])
def user_order():
    if request.method == "POST":
        user_JWT = request.cookies.get('user_token')
        if user_JWT == None:
            response = make_response(json.dumps({"data":None}))
            response.headers['Access-Control-Allow-Origin']=request_url
            response.headers['Access-Control-Allow-Credentials']= "true"
            return response
        order_info = json.loads(request.data)
        decoded_JWT = decode_user_JWT(user_JWT)
        print(order_info)
        trade_info = {
            "prime":order_info["prime"],
            "phone":order_info["order"]['contact']["phone"],
            "user_name":order_info["order"]['contact']["name"],
            "email":order_info["order"]['contact']["email"],
        }
        response = trade_order(trade_info)
        trade_stsuts = response[0]
        if trade_stsuts:
            order_info["number"] = response[1]
            order_info["status"] = 0
            print(order_info)
            code, message = creat_order(order_info)
            if code == 200:
                delete_booking(order_info["order"]['contact']["email"])
                response = make_response(json.dumps(message))
                response.headers['Access-Control-Allow-Origin']=request_url
                response.headers['Access-Control-Allow-Credentials']= "true"
                return response
            else:
                message = {"error":True, "message":message}
                response = make_response(json.dumps(message))
                response.headers['Access-Control-Allow-Origin']=request_url
                response.headers['Access-Control-Allow-Credentials']= "true"
                return response
        else:
            message = {"error":True, "message":response[1]}
            response = make_response(json.dumps(message))
            response.headers['Access-Control-Allow-Origin']=request_url
            response.headers['Access-Control-Allow-Credentials']= "true"
            return response
        
    if request.method == "OPTIONS":
        message = {"ok":True}
        header_request_method = request.headers['Access-Control-Request-Method']
        # request_url = request.headers['Origin']
        response = make_response(json.dumps(message))
        response.headers['Access-Control-Allow-Origin']=request_url
        response.headers['Access-Control-Allow-Credentials']= "true"
        response.headers['Access-Control-Allow-Methods']= header_request_method
        return response

@app_api_order.route("/orders/<orderNumber>", methods=['GET','POST','DELETE','OPTIONS'])
def user_order_id(orderNumber):
    if request.method == "GET":
        user_JWT = request.cookies.get('user_token')
        if user_JWT == None:
            response = make_response(json.dumps({"error":True, "message":"未登入系統，拒絕存取"}))
            response.headers['Access-Control-Allow-Origin']=request_url
            response.headers['Access-Control-Allow-Credentials']= "true"
            return response
        decoded_JWT = decode_user_JWT(user_JWT)
        code, data = read_order_by_number(orderNumber)
        print(data)
        response = make_response(json.dumps(data))
        response.headers['Access-Control-Allow-Origin']=request_url
        response.headers['Access-Control-Allow-Credentials']= "true"
        return response