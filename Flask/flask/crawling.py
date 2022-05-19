# 크롤링 라이브러리 import
import requests
from bs4 import BeautifulSoup


def today_humor() :
    # 엔터치기
    req = requests.get('http://www.todayhumor.co.kr/board/list.php?table=bestofbest')

    # 이런 식으로 HTML에 있는 코드를 다 가져온다
    soup = BeautifulSoup(req.text, 'html.parser')

    myList = []

    for i in soup.find_all("td", class_="subject") :
        myList.append(i.text)

    return myList


def clien():
    # 엔터치기
    req = requests.get('https://www.clien.net/service/recommend')

    # 이런 식으로 HTML에 있는 코드를 다 가져온다
    soup = BeautifulSoup(req.text, 'html.parser')

    myList = []

    for i in soup.find_all("span", class_="subject_fixed") :
        myList.append(i.text)

    return myList