from flask import Flask, render_template, request
import requests
import json
import secrets

app = Flask(__name__)

# 暗号化キー
app.secret_key = secrets.token_urlsafe(32)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def post():
    if request.form["animal"] == "cat":
        res = requests.get("https://api.thecatapi.com/v1/images/search")
        outfile = json.loads(res.text)[0]["url"]
    elif request.form["animal"] == "dog":
        res = requests.get("https://dog.ceo/api/breeds/image/random")
        outfile = json.loads(res.text)["message"]
    else:
        res = requests.get("https://randomfox.ca/floof")
        outfile = json.loads(res.text)["image"]
    return render_template("upload.html", outfile=outfile)


if __name__ == "__main__":
    app.run(debug=True)
