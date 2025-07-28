from spitch import Spitch
from flask import Flask, request, render_template, make_response
from datetime import datetime
import os
import json

os.environ["SPITCH_API_KEY"] = "REPLACE WITH YOUR API KEY."
client = Spitch()

app = Flask(__name__)

def translate(text, target_language):
    if target_language == "en":
        return text
    else:
        return client.text.translate(text=text, source='en', target=target_language).text
    
def say_hello(name):
    return f"Hello there, {name}! It's {datetime.now().strftime('%A, %d %B, %Y at %X')}."

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/hello", methods=["POST"])
def index():
    if request.method == "POST":
        data = request.get_json()
        name = data.get("name", "")
        target_language = data.get("language", "en")

        
        greeting = translate(say_hello(name), target_language)
        
        response = make_response(json.dumps({"greeting": greeting}))
        response.headers["Content-Type"] = "application/json"
        
        return response

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)