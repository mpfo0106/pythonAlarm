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

def likey(insta_tag):
    total_cnt = random.randrange(20, 40)
    driver.get(f'https://www.instagram.com/explore/tags/{insta_tag}/')
    time.sleep(10)
    like_cnt = 0
    overlap_cnt = 0
    new_feed = driver.find_elements(By.CLASS_NAME, 'eLAPa')[9]
    new_feed.click()

    for i in range(total_cnt):
        time.sleep(3)
        span = driver.find_element(By.CSS_SELECTOR, 'span.fr66n')

        # '/html/body/div[6]/div[3]/div/article/div/div[3]/div/div/section[1]/span[1]'
        like_btn = span.find_element(By.TAG_NAME, 'button')
        btn_svg = like_btn.find_element(By.TAG_NAME, 'svg')
        isLike = btn_svg.get_attribute('aria-label')

        if isLike == '좋아요':
            overlap_cnt = 0
            like_btn.click()
            print(f'{like_cnt} 번째 좋아요를 눌렀습니다')
            like_cnt += 1
            time.sleep(random.randrange(5))
        else:
            print('이미 누른 좋아요입니다')
            time.sleep(random.randrange(5))
            overlap_cnt += 1
            if overlap_cnt >3 :
                print(f'중복 좋아요가 {overlap_cnt} 개 입니다')
                break

        if i < total_cnt - 1:
            next_feed_div = driver.find_element(By.XPATH, '/html/body/div[6]/div[2]/div/div[2]')
            next_feed = next_feed_div.find_element(By.TAG_NAME, 'button')
            next_feed.click()
            time.sleep(random.randrange(10))

login(id,pw)
while True:
    #hashList = "#airforce1 #airforce1mid #stuusy  #stussyairforce1mid #신발스타그램 #나이키 #스투시 #스투시포스 #스투시에어포스 #스투시에어포스1포실 #나이키스투시 #에어포스1 #에어포스1미드 #나투시 #stussynike #nikestussy #nikestyleclub #airforce1 #airforce1mid #sneakerhead #sneakerheads #airforce #kickstagram #thekickscafe #snkerskickcheck #snkrs"
    #hashList ='#조던#조던1#조던1로우#조던1라이트스모크그레이#조던1라이트스모크그레이블랙 #쉐도우토 #조던1로우쉐도우토 #신발스타그램#jordan1 #jordan1low #shadowtoe #jordans #j1 #j1low #snkrs #sneakers #nike#Jordan1ShadowToe #JordanManila #Shoegame #SneakerHustle #Dunks #Sneakerheads '
    hashList = '#좋반 #좋아요반사 #맞팔 #선팔 #선팔하면맞팔'
    insta_tag = hashtagParser(hashList) # 파싱해서옴
    shuffle_tag = random.sample(insta_tag, len(insta_tag)) #셔플은 변경할 수 없는 리스트를 섞지 못해 그래서 sample 을 써야해
    for tag in shuffle_tag:
        try:
            print(f"작업태그는 {tag} 입니다")
            likey(tag)
        except :
            print("오류가 발생해서 다음 태그로 넘어갑니다.")
            driver.refresh()
    print("모든 작업이 끝났습니다")
    driver.quit()

