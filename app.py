from flask import Flask , request , jsonify
from pymongo import MongoClient
from flask_cors import CORS
app = Flask(__name__)

CORS(app)


client = MongoClient("mongodb+srv://sriram65raja:1324sriram@cluster0.dejys.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
NAMES = client["ai"]
URL_DATA = NAMES["URL_DATA"]

@app.route("/")
def home():
    return "Running Suessfully 🤑"

@app.route("/get-url")
def url_get():
    url = request.args.get("url")
    if not url:
        return jsonify("ERror")
    data = {
        "url":url
    }
    
    URL_DATA.insert_one(data)
    
    return jsonify({"VISIT" : "/find"})

@app.route("/find")
def finds():
    data_url = list(URL_DATA.find({} , {"_id":0}).sort("_id" , -1).limit(1))
    return jsonify(data_url)
    

    

if __name__ == "__main__":
    app.run()
