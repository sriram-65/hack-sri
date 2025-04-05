from flask import Flask , request , jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Running Suessfully 🤑"

@app.route("/get-url" , methods=["POST" ,"GET"])
def url_get():
    if request.method == "POST":
         url = request.json.get("url")
         if not url:
           return "Url is Must"
    return jsonify({"URL_IS_GENERATED " : url })

    

if __name__ == "__main__":
    app.run()
