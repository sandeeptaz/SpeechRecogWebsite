from flask import Flask,render_template,url_for,request
import pymongo
from flask_cors import CORS
import json, ast


app = Flask(__name__)
CORS(app)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Webstore"]
storesColl = mydb["stores"]



@app.route('/speech',methods=['POST'])
def uploadz():
	print("Hello world")
	data = request.get_json()
	raw = ast.literal_eval(json.dumps(data))
	speechtext = raw["speechtext"] 
	resp = storesColl.find_one({ "$text": { "$search":speechtext } })	  
	return resp

if __name__ == '__main__':
	app.run(debug=True)