from flask import *
from api.attractions import app_api_attractions
from api.userapi import app_api_user
from api.booking import app_api_booking
from api.orders import app_api_order

app=Flask(__name__)
app.config["JSON_AS_ASCII"]=False
app.config["TEMPLATES_AUTO_RELOAD"]=True
app.register_blueprint(app_api_attractions)
app.register_blueprint(app_api_user)
app.register_blueprint(app_api_booking)
app.register_blueprint(app_api_order)
# Pages
@app.route("/")
def index():
	return render_template("index.html")
@app.route("/attraction/<id>")
def attraction(id):
	return render_template("attraction.html")
@app.route("/booking")
def booking():
	return render_template("booking.html")
@app.route("/thankyou")
def thankyou():
	return render_template("thankyou.html")

app.run(port=3000, debug=True)