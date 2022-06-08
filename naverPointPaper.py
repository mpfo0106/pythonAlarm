import chromedriver_autoinstaller
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyperclip

url_list = ["https://ofw.adison.co/u/naverpay/ads/55162",
            "https://ofw.adison.co/u/naverpay/ads/66420",
            "https://ofw.adison.co/u/naverpay/ads/67823",
            "https://ofw.adison.co/u/naverpay/ads/72557"]

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]  #크롬드라이버 버전 확인
try:
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe')
except:
    chromedriver_autoinstaller.install(True) #현재 파이썬 파일이 있는 곳에 크롬 버전을 폴더 이름으로 하여 크롬드라이버가 그 안에 저장
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe')

driver.implicitly_wait(10)

login = {
    "id" : "mpfo551",
    "pw" : "joonho0786!"
}

def clipboard_input(user_xpath, user_input):
    temp_user_input = pyperclip.paste()  # 사용자 클립보드를 따로 저장

    pyperclip.copy(user_input)
    driver.find_element(By.XPATH, user_xpath).click()
    ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

    pyperclip.copy(temp_user_input)  # 사용자 클립보드에 저장 된 내용을 다시 가져 옴
    time.sleep(1)

def naver_pay_click(url):
    driver.get(url)
    try:
        clipboard_input('//*[@id="id"]', login.get("id"))
        clipboard_input('//*[@id="pw"]', login.get("pw"))
        driver.find_element(By.XPATH, '//*[@id="log.login"]').click()
    except:
        pass
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div/div/button').click()
    time.sleep(1)

for i in range(4):
    url = url_list[i]
    naver_pay_click(url)

driver.quit()