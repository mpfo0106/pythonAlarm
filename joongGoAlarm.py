import random
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pyperclip

import sys
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from slack_sdk import WebClient #슬랙
from slack_sdk.errors import SlackApiError #슬랙 에러

chromeW_options = webdriver.ChromeOptions()
chromeW_options.add_argument("--disable-extensions")
#chromeW_options.headless = True
chromeW_options.add_argument("window-size=2560x1600")
chromeW_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36")
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"}


chromeL_options = webdriver.ChromeOptions()
chromeL_options.add_argument('--headless')
chromeL_options.add_argument('--no-sandbox')
chromeL_options.add_argument('--disable-dev-shm-usage')
chromeL_options.add_argument("user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'")

if sys.platform == 'linux':
  driver = webdriver.Chrome('/home/ubuntu/alarm/pythonAlarm/chromedriver',options=chromeL_options)
else :
  driver = webdriver.Chrome('./chromedriver',options=chromeW_options)

slack_token = 'xoxb-3594636446836-3585655033366-cCZdlQLoYNlI65TkreS5oCDK'
client = WebClient(token=slack_token) # 슬랙 생성

# def naverLogin():
#     url = 'https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com'
#     driver.get(url)
#     driver.implicitly_wait(1)
#     naver_id = 'mpfo551'
#     naver_pw = 'joonho0786!'
#     pyperclip.copy(naver_id)
#     driver.find_element(By.XPATH,'//*[@id="id"]').send_keys(Keys.CONTROL + 'v')
#     pyperclip.copy(naver_pw)
#     driver.find_element(By.XPATH,'//*[@id="pw"]').send_keys(Keys.CONTROL + 'v')
#     time.sleep(0.7)
#     driver.find_element(By.XPATH,'//*[@id="log.login"]').click()
#     time.sleep(1)


# flag = 0
# def job_function():
#     if tmp_list:
#         for index,url in enumerate(tmp_list):
#             delIndex = check_restock(index,url)
#             del tmp_list[delIndex]
#     else:
#         sched.pause()
#
# def job_restart():
#     tmp_list.extend(url_list)
# def check_exists_by_CSS(css):
#     try:
#         driver.find_elements(By.CSS_SELECTOR, css)
#     except NoSuchElementException:
#         return False
#     return True

def check_alarm(url,title):
    driver.get(url + '?iframe_url=/ArticleList.nhn%3Fsearch.clubid=10050146%26search.menuid=334%26search.boardtype=I')
    #driver.get(url+'/ArticleList.nhn?search.clubid='+clubid+'&search.boardtype=L')
    driver.implicitly_wait(4)
    driver.switch_to.frame('cafe_main') #ifame 변경!
    soup = BeautifulSoup(driver.page_source,'lxml')
    time.sleep(2)
    articles = soup.select('#main-area > ul.article-album-sub > li:nth-child')
    for article in articles:
        page = article.select_one('td.td_article > div.board-list > div > a') #select_one 주의!
        titleTmp =page.get_text().replace("\n", "").strip()
        #print(title)
        try:
            for keyWord in keyWords:
                if(f'{keyWord}' in titleTmp) and (titleTmp not in title):
                    link = page.get('href') #.get으로 href 뽑아오기
                    response = client.chat_postMessage(channel='navercafe',
                                                       text=f"{titleTmp} \n {baseUrl+ link}")
                    title.append(titleTmp)
                else:
                    continue
        except SlackApiError as e:
            print('Error: {}'.format(e.response['error']))

    return title

title = []
keyWords = ['크림','ㅎㅈ','홍조','ㅎㄴ','홍나','ㅎㅍ','홍풋','신풋','ㅅㅍ','ㅅㅈ','서조','두타','ㄷㅌ','ㅌㅋ','탐퀘','ㅅㄴ','서나','ㄱㄴ','강나','ㅁㄴ','명나','ㅇㅅ','용산','뛰어','뛰','달려']
baseUrl = 'https://cafe.naver.com/joonggonara'
clubid = '10050146'
#naverLogin()
while(True):
    check_alarm(baseUrl,title) # 전체글보기 정확한 url 을 타겟팅 해줘야해
    if len(title) >15:
        del title[0]
    time.sleep(random.randrange(10,30))


