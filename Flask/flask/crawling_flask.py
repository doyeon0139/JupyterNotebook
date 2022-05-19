from flask import Flask, render_template
app = Flask(__name__)

import crawling


@app.route('/')
def hello():

    # myList = crawling.daum()
    todayhumor = crawling.today_humor()
    clien = crawling.clien()

    return render_template("index3.html", list2 = todayhumor, list3 = clien)

@app.route('/about')
def about():
    return "여기는 어바웃입니다."


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='8080')