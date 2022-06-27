import unicodedata
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random

options = webdriver.ChromeOptions()

options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25")
options.add_argument("--start-maximized")


###
driver = webdriver.Chrome('chromedriver.exe', options=options)
driver.get('https://instagram.com')
time.sleep(5)
id = 'milk.budan'
pw = 'joonho0786!'

def hashtagParser(hashList):
    hashSplit = hashList.split('#')
    i = 0
    while i < len(hashSplit):
        if hashSplit[i] == '':
            del hashSplit[i]
        else:
            hashSplit[i] = hashSplit[i].strip()
            i += 1
    return hashSplit


def login(id,pw):
    btn = driver.find_elements(By.TAG_NAME, 'button')[1]
    btn.click()

    inputbox = driver.find_elements(By.TAG_NAME, 'input')[0]
    inputbox.click()
    inputbox.send_keys(id)

    inputbox = driver.find_elements(By.TAG_NAME, 'input')[1]
    inputbox.click()
    inputbox.send_keys(pw)

    inputbox.send_keys(Keys.ENTER)

    time.sleep(5)

def detect_ad():
    ad_list = ['재테크', '투자', '부업', '집테크', '고수입', '수입', '억대연봉', '억대', '연봉', '순수익', '초기금액', '초기 금액', '금액', '입금']
    try :
        driver.find_element(By.XPATH,'//*[text() = "더 보기"]').click()
        pass
    except:
        pass
    texts = driver.find_elements(By.XPATH,'//span//span')
    for text in texts :
        article = unicodedata.normalize('NFC',text.get_attribute('innerText'))
        for ad in ad_list :
            if article.find(ad) == -1 :
                continue
            else :
                print(f'광고 발견으로 통과합니다. 발견된 광고단어 : {ad}')
                return True


def likey(insta_tag):
    like_cnt = random.randrange(20, 30)
    driver.get('https://www.instagram.com/explore/tags/{}/'.format(insta_tag))
    time.sleep(random.randrange(5, 15))

    new_feed = driver.find_elements(By.CLASS_NAME,'_aagu')[9]
    new_feed.click()

    numoflike = 0
    stop_num = 0
    for i in range(like_cnt):
        time.sleep(3)
        span = driver.find_element(By.XPATH, '//*[@aria-label="좋아요" or @aria-label="좋아요 취소"]//ancestor :: span[2]') # 좋아요 위에 span을 따야지 좋아요 여부에 상관없이 클릭 가능
        like_btn = span.find_element(By.TAG_NAME,'button') # 버튼 위치 따고
        btn_svg = like_btn.find_element(By.TAG_NAME, 'svg') # svg 따고
        svg = btn_svg.get_attribute('aria-label') # svg 의 내용이 좋아요 인지 좋아요 취소 인지 저장

        if detect_ad() == True:
            driver.find_element(By.XPATH,'//*[@aria-label="다음" and @height="16"]//ancestor :: div[2]').click()
            time.sleep(2)
            continue

        elif svg == '좋아요':
            like_btn.click()
            numoflike += 1
            print('좋아요를 {}번째 눌렀습니다.'.format(numoflike))
            time.sleep(random.randrange(20, 50))
        else:
            print('이미 작업한 피드입니다.')
            time.sleep(random.randrange(5))
            stop_num += 1
            if stop_num > 3:
                print(f'좋아요 누른 태그가 {stop_num}개 중복됩니다.')
                break

        if i < like_cnt - 1:
            next_feed_xpath = driver.find_element(By.XPATH, '//*[@aria-label="다음" and @height="16"]//ancestor :: div[2]') # 버튼 찾기 위해 위로 두개 올라간 태그 따기
            next_feed = next_feed_xpath.find_element(By.TAG_NAME, 'button') #버튼 따고
            next_feed.click() # 다음 버튼 클릭
            time.sleep(random.randrange(5))

login(id,pw)
while True:
    #hashList = "#airforce1 #airforce1mid #stuusy  #stussyairforce1mid #신발스타그램 #나이키 #스투시 #스투시포스 #스투시에어포스 #스투시에어포스1포실 #나이키스투시 #에어포스1 #에어포스1미드 #나투시 #stussynike #nikestussy #nikestyleclub #airforce1 #airforce1mid #sneakerhead #sneakerheads #airforce #kickstagram #thekickscafe #snkerskickcheck #snkrs"
    hashList = "#yeezyfoamrunner #yeezyfoams #yeezyfoamsandgrey #foamrnnr #foamrnnrsandgrey#yeezy #yeezymafia#sneakerheads #kicksonfire #atmosthailand #carnivalbkk#adidas #adidasthailand#nike #nikethailand #sasom #nationofsoles#walklikeus #complexsneakers #complexkicks #dailysole#nicekicks #sneakers #hypebeast #sneakergallery#sneakerfiles #streetwear #uksneakerhead #조던1 #나이키 #이지부스트 #폼러너 #오닉스 #foamrunner #이지"
    #hashList ='#조던#조던1#조던1로우#조던1라이트스모크그레이#조던1라이트스모크그레이블랙 #쉐도우토 #조던1로우쉐도우토 #신발스타그램#jordan1 #jordan1low #shadowtoe #jordans #j1 #j1low #snkrs #sneakers #nike#Jordan1ShadowToe #JordanManila #Shoegame #SneakerHustle #Dunks #Sneakerheads '
    #hashList = '#좋반 #좋아요반사 #맞팔 #선팔 #선팔하면맞팔'
    insta_tag = hashtagParser(hashList) # 파싱해서옴
    shuffle_tag = random.sample(insta_tag, len(insta_tag)) #셔플은 변경할 수 없는 리스트를 섞지 못해 그래서 sample 을 써야해
    for tag in shuffle_tag:
        try:
            print(f'작업 태그는 {tag} 입니다.')
            likey(tag)
            print(f'{tag} 태그 작업이 끝났습니다. 다음 태그로 넘어갑니다.')
        except:
            print('새로운 피드가 없거나, 다음 피드가 없습니다. 다음 태그로 넘어갑니다.')
            driver.refresh()
    driver.quit()

