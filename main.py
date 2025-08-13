# from flask import Flask, render_template
from flask import Flask, render_template, jsonify
import requests


app = Flask(__name__)

@app.route("/")
def home():
  return render_template('index.html')

@app.route("/get_meme")
def get_meme():
    response = requests.get("https://meme-api.com/gimme")
    data = response.json()
    return jsonify({
        "title": data["title"],
        "url": data["url"]
    })

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080, debug = True)
