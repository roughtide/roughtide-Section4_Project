from selenium import webdriver
import time
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(executable_path='C:\\Develop\\Project4\\chromedriver.exe', options=options)


pages = range(36337, 36745)
videoIds = []
for page in pages:
    webpage = "https://www.fss.or.kr/fss/bbs/B0000206/view.do?nttId=%d&menuNo=200690"%(page)
    driver.get(webpage)
    req = driver.page_source
    soup = BeautifulSoup(req, 'lxml')
    
    videos = soup.select('#content > div.bd-view > div > video')[0]['src']
    split = videos.split('FileId=')[1]
    videoId = split.split('&fileSn=')[0]
    videoIds.append(videoId)


