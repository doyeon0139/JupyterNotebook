from flask import Flask, render_template

import selenium
from bs4 import BeautifulSoup
from selenium import webdriver

import time

app = Flask(__name__)

@app.route('/clien')
def clien():
    url = 'https://www.clien.net/service/recommend'

    driver = webdriver.Chrome()

    time.sleep(1)
    driver.get(url)
    time.sleep(3)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    print(soup)

    myList = []

    # path = '#news > div.news_prime.news_tab2 > div > ul > li > a'
    path = 'span.subject_fixed'

    for i in soup.select(path):
        myList.append(i.text)
        print(i.text)
    # print('========')
    # print(myList)
    return myList

@app.route('/today_humor')
def today_humor():
    url = 'http://www.todayhumor.co.kr/board/list.php?table=bestofbest'

    driver = webdriver.Chrome()

    time.sleep(1)
    driver.get(url)
    time.sleep(3)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    print(soup)

    myList1 = []

    # path = '#news > div.news_prime.news_tab2 > div > ul > li > a'
    path = 'td.subject'

    for i in soup.select(path):
        myList1.append(i.text)
        print(i.text)
    # print('========')
    # print(myList)
    return myList1

@app.route('/all')
def all_contents():
    _, myList = clien()
    _, myList1 = today_humor()
    return render_template('index2.html', list = myList, list1 = myList1)

@app.route('/about')
def about():
    return "about page입니다.."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080')