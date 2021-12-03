from flask import Flask
from flask import render_template
from flask import request
from functions import tweet ,JA_to_EN

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/twitter",methods=["GET","POST"])
def twitter():
    sitename = request.form.get("sitename")
    return render_template("twitter.html",sitename=sitename)


@app.route("/movie",methods=["GET","POST"])
def movie():
    sitename = request.form.get("sitename")
    return render_template("movie.html",sitename=sitename)

@app.route("/ja_to_en",methods=["GET","POST"])
def ja_to_en():
    sitename = request.form.get("sitename")
    return render_template("ja_to_en.html",sitename=sitename)

@app.route("/result",methods=["GET","POST"])
def result():
    # tweet.py呼び出し
    JA_to_EN.ja_to_en()
    sitename = request.form.get("sitename")
    return render_template("result.html",sitename=sitename)




if __name__ == '__main__':
    app.run()