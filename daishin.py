from selenium import webdriver
from bs4 import BeautifulSoup
import time
import codecs
import os
import pickle
import requests
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
#chrome_options.add_argument("--user-data-dir=chrome-data")
chrome_options.add_argument("user-data-dir=selenium") 
driver = webdriver.Chrome('D:/chrome/chromedriver',options=chrome_options)
driver.implicitly_wait(3)
driver.get("https://www.daishin.com/nsl/service/hts/itemDesc.ds?p=7976&v=7266&m=8706&xfsid=EtGuNefjQC2hkYcpEuhIXQ")

time.sleep(100)
print('START===>')

def article_Scraping():
    num=0
    while True:
      num += 1
      print('시작===>')
      print(num)
      #driver.get("https://www.daishin.com/nsl/service/hts/itemDesc.ds?p=7976&v=7266&m=8706&xfsid=EtGuNefjQC2hkYcpEuhIXQ")
      #driver.refresh()
      #driver.get(driver.current_url)
      driver.execute_script("location.reload()")
      #driver.get("http://211.240.100.206/")
      #print(articles.find_element_by_tag_name("th").text
      html = driver.page_source
      #print(html)
      #driver.page_source.encode('ascii', 'ignore')
      soup = BeautifulSoup(html, 'html.parser')
      f = open("D:/web/test.html",'w',encoding='utf-8')
      f.write(html)
      f.close
      print('완료===>')
      time.sleep(60)


article_Scraping()