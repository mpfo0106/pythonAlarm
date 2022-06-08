from selenium import webdriver
import chromedriver_autoinstaller
import subprocess
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pyperclip
import time
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup as bs
import requests



chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]  #크롬드라이버 버전 확인
try:
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe')
except:
    chromedriver_autoinstaller.install(True) #현재 파이썬 파일이 있는 곳에 크롬 버전을 폴더 이름으로 하여 크롬드라이버가 그 안에 저장
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe')

driver.implicitly_wait(10)



# subprocess.Popen 은 크롬 브라우저를 실행시키는 명령어
# --remote-debugging-port=9222 : 구동하는 크롬의 포트를 알려주는 것이다
# –user-data-dir=”C:\chrometemp” 는 크롬을 사용하여 웹상을 돌아다녔을 때 생기는 쿠키와 캐쉬파일을 저장
subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chrometemp"') # 디버거 크롬 구동

option = Options()
option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
try:
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
except:
    chromedriver_autoinstaller.install(True)
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
driver.implicitly_wait(10)


driver.get("https://naver.com")

# 라디오 버튼 클릭
# button =driver.find_element(By.XPATH,'//*[@id="keep"]')
# driver.execute_script("arguments[0].click();", button)