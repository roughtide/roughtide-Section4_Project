from selenium import webdriver
import time
from urllib import request
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(executable_path='C:\\Develop\\Project4\\chromedriver.exe', options=options)

title_lists = []

for pageIndex in range(1,24):
    webpage = "https://www.fss.or.kr/fss/bbs/B0000207/list.do?menuNo=200691&pageIndex=%d"%(pageIndex)
    driver.get(webpage)
    req = driver.page_source
    soup = BeautifulSoup(req, 'lxml')
    titles = soup.select_one('#content > div.bd-list')
    titles = titles.select('table > tbody > tr > td > a')
    for i in range(len(titles)):
        split = titles[i]['href'].split('nttId=')[1]
        listId = split.split('&menuNo=')[0]
        title_lists.append(listId)

videoIds = []

for page in title_lists:
    webpage = "https://www.fss.or.kr/fss/bbs/B0000207/view.do?nttId=%s&menuNo=200691"%(page)
    driver.get(webpage)
    req = driver.page_source
    soup = BeautifulSoup(req, 'lxml')
    
    videos = soup.select('#content > div.bd-view > div > video')[0]['src']
    split = videos.split('FileId=')[1]
    videoId = split.split('&fileSn=')[0]
    videoIds.append(videoId)
    time.sleep(3)

print(videoIds) 

i = 0
for vid in videoIds:
    num = str(i).zfill(3)
    url = "https://www.fss.or.kr/fss/cmmn/file/fileDown.do?menuNo=200690&atchFileId=%s&fileSn=1&bbsId=B0000206"%(vid)
    savename = "C:\\Develop\\Project4\\mortgagefraud\\mortgage_fraud_%s.mp3"%(num)
    request.urlretrieve(url,savename)
    time.sleep(2)
    i += 1