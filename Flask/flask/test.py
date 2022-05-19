
import selenium
from bs4 import BeautifulSoup
from selenium import webdriver
import time

url = 'https://www.daum.net'

driver = webdriver.Chrome()

driver.get(url)
time.sleep(2)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

print(soup)