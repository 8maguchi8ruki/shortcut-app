from flask import Flask
from flask import render_template
from flask import request
from functions import twitter ,JA_to_EN

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tweet",methods=["GET","POST"])
def tweet():
    sitename = request.form.get("sitename")
    return render_template("tweet.html",sitename=sitename)


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
    form_value = request.form.get("text")
    if(form_value == "tweet"):
        twitter.post_tweet(form_value)
    elif(form_value == "ja_to_en"):
        JA_to_EN.ja_to_en(form_value)
    return render_template("result.html")




if __name__ == '__main__':
    app.run()
