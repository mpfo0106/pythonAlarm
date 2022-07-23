import random
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import chromedriver_autoinstaller
import telegram
import pyperclip
import passWord
import sys
import passWord
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


chromeW_options = webdriver.ChromeOptions()
chromeW_options.add_argument("--disable-extensions")
chromeW_options.headless = True
chromeW_options.add_argument("window-size=2560x1600")
chromeW_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36")
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"}


chromeL_options = webdriver.ChromeOptions()
chromeL_options.add_argument('--headless')
chromeL_options.add_argument('--no-sandbox')
chromeL_options.add_argument('--disable-dev-shm-usage')
chromeL_options.add_argument("--single-process")
chromeL_options.add_argument("user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'")

if sys.platform == 'linux':
    driver = webdriver.Chrome("/home/ubuntu/alarm/pythonAlarm/chromedriver",options=chromeL_options)
else :
    chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]  # 크롬드라이버 버전 확인
    try:
        driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe',options=chromeW_options)
    except:
        chromedriver_autoinstaller.install(True)
        driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe',options=chromeW_options)


token = passWord.tele_offline_run_token
id = 1905923211
bot = telegram.Bot(token)

# bot.sendMessage(chat_id=id, text="테스트 중입니다.")
def login(id,pw):
    driver.get('https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')
    naver_id = 'mpfo551'
    naver_pw = 'joonho0786!'
    pyperclip.copy(naver_id)
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="id"]').send_keys(Keys.CONTROL + 'v')

    pyperclip.copy(naver_pw)
    driver.find_element(By.XPATH, '//*[@id="pw"]').send_keys(Keys.CONTROL + 'v')
    time.sleep(0.7)
    driver.find_element(By.XPATH, '//*[@id="log.login"]').click()
    driver.implicitly_wait(2)

    # driver.find_element(By.XPATH, '//*[@id = "new.save"]').click()
    # time.sleep(2)
    # driver.switch_to.window(tabs[0])

def check_alarm(url,title):
    driver.get(url+'/ArticleList.nhn?search.clubid='+clubid+'&search.boardtype=L')
    driver.implicitly_wait(4)
    driver.switch_to.frame('cafe_main') #ifame 변경!
    soup = BeautifulSoup(driver.page_source,'lxml')
    time.sleep(2)
    articles = soup.select('#main-area > div:nth-child(4) > table > tbody > tr')
    for article in articles:
        page = article.select_one('td.td_article > div.board-list > div > a') #select_one 주의!
        titleTmp =page.get_text().replace("\n", "").strip()
        #print(title)
        for keyWord in keyWords:
            if(f'{keyWord}' in titleTmp) and (titleTmp not in title):
                link = page.get('href') #.get으로 href 뽑아오기
                response = bot.sendMessage(chat_id=id, text=f"{titleTmp} \n {baseUrl+ link}")
                title.append(titleTmp)
            else:
                continue
    return title

title = []
keyWords = ['.','ㅎㅈ','홍조','ㅎㄴ','홍나','ㅎㅍ','홍풋','신풋','ㅅㅍ','ㅅㅈ','서조','두타','ㄷㅌ','ㅌㅋ','탐퀘','ㅅㄴ','서나','ㄱㄴ','강나','ㅁㄴ','명나','ㅇㅅ','용산','뛰어','뛰','달려']
baseUrl = 'https://cafe.naver.com/ofad'
clubid = '29331308'
#naverLogin()
while(True):
    login(passWord.my_naver_id,passWord.my_naver_pw)
    check_alarm(baseUrl,title) # 전체글보기 정확한 url 을 타겟팅 해줘야해
    if len(title) >15:
        del title[0]
    time.sleep(random.randrange(10,30))


