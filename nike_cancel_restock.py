import random
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import telegram as tele
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from apscheduler.schedulers.blocking import BlockingScheduler
bot = tele.Bot(token="5357762614:AAFyDNGu_baMCtwvVtzMWEfkEjdJgXSS0uQ")  # HTTP token입력
chat_id = 1905923211 #채팅아이디(고정으로 쓸 경우)
# chat_id = bot.getUpdates()[-1].message.chat.id  # 가장 최근에 온 메세지의 정보 중, chat id만 가져옴

options = webdriver.ChromeOptions()
#options.add_argument("--disable-extensions")
options.headless = True
options.add_argument("window-size=2560x1600")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36")
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"}
browser = webdriver.Chrome(options=options)

url_list = ["https://www.nike.com/kr/ko_kr/t/men/fw/nike-sportswear/CW2288-111/avbt44/air-force-1-07",
                "https://www.nike.com/kr/ko_kr/t/men/fw/nike-sportswear/DH7579-100/yyV9h5GC2/air-force-1-07-prm",
            "https://www.nike.com/kr/ko_kr/t/junior/fw/young-athletes/DM0984-700/SxO6f37rY8y/air-force-1-lv8-nn-gs"]
tmp_list = url_list
flag = 0
def job_function():
    if tmp_list:
        for index,url in enumerate(tmp_list):
            delIndex = check_restock(index,url)
            del tmp_list[delIndex]
    else:
        sched.pause()

def job_restart():
    tmp_list.extend(url_list)

def create_soup(url):
    res = requests.get(url, headers= headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup

# def check_exists_by_CSS(css):
#     try:
#         browser.find_elements(By.CSS_SELECTOR, css)
#     except NoSuchElementException:
#         return False
#     return True

def check_restock(index,url):
    browser.get(url)
    name = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/section/section/section/article/article[2]/div/div[4]/div/div[1]/h1/span")))
    time.sleep(2)
    shoes = browser.find_elements(By.CSS_SELECTOR, "span.input-radio")
    browser.implicitly_wait(2)
    for shoe in shoes:
        try:
            browser.implicitly_wait(1)
            shoe.find_element(By.CSS_SELECTOR, "label.sd-out")
        except NoSuchElementException:
            bot.sendMessage(chat_id, text= f"{name.text} {shoe.text} 리스탁 \n {url}")
            print()
    print()
    browser.delete_all_cookies()
    return index

sched = BlockingScheduler(timezone='Asia/Seoul')

sched.add_job(job_function, 'interval', seconds=30, max_instances=5)
sched.add_job(job_restart, 'interval', minutes=30)
sched.start()




#  Pythonanywhere 사용해서 서버에서 돌리기, 왜 바로 끝나는지 분석