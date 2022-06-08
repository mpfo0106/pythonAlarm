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

# 불필요한 메세지 없애기


#  로그인
class login():
    def naver_login(self):

        # 페이지가 완전히 로딩되도록 3초동안 기다림
        time.sleep(1)
        naver_id = 'mpfo551'
        naver_pw = 'joonho0786!'

        pyperclip.copy(naver_id)
        driver.find_element(By.XPATH, '//*[@id="id"]').send_keys(Keys.CONTROL + 'v')
        time.sleep(1)

        pyperclip.copy(naver_pw)
        driver.find_element(By.XPATH, '//*[@id="pw"]').send_keys(Keys.CONTROL + 'v')
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="log.login"]').click()

    def nike_login(self):
        ## 나이키 로그인
        nike_id = 'jade1007@naver.com'
        nike_pw = 'joonho7878!'

        driver.get('https://www.nike.com/kr/ko_kr/')
        driver.implicitly_wait(20)
        driver.find_element(By.XPATH, '//*[@id="j_username"]').send_keys(nike_id)
        driver.find_element(By.XPATH, '//*[@id="j_password"]').send_keys(nike_pw)
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="common-modal"]/div/div/div/div[2]/div/div[2]/div/button').click()

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

###########

my_login = login()

# # 네이버 로그인
# driver.get('https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')
# time.sleep(0.5)
# button =driver.find_element(By.XPATH,'//*[@id="keep"]')
# driver.execute_script("arguments[0].click();", button)
# driver.find_element(By.XPATH, '//*[@id="log.login"]').click()
#
# #뉴릴 이동
# driver.get('https://www.nike.com/kr/ko_kr/w/xg/xb/xc/new-releases?productCategoryType=FW')
#
#
# # 뉴릴 제목 조회
# nike_fw_url = 'https://www.nike.com/kr/ko_kr/w/xg/xb/xc/new-releases?productCategoryType=FW'
# response = requests.get(nike_fw_url)
# html_text = response.text
# soup = bs(response.text, 'html.parser')

id = 'jade1007'
pw = 'joonho7878!'

try:
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, 'login')))
    elem_btn = driver.find_element(By.CLASS_NAME, 'login')
    elem_btn.click() # 버튼 클릭

    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'j_username')))
    elem_id = driver.find_element(By.ID, 'j_username')
    elem_id.send_keys(id) # id 입력

    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'j_password')))
    elem_pw = driver.find_element(By.ID, 'j_password')
    elem_pw.send_keys(pw)

    login_btn = driver.find_element(By.XPATH, '//button[@class="button large width-max"]')
    login_btn.click()
except: # 이미 로그인이 되어있는 경우
    pass




# 라디오 버튼 클릭
# button =driver.find_element(By.XPATH,'//*[@id="keep"]')
# driver.execute_script("arguments[0].click();", button)