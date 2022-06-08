from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException, UnexpectedAlertPresentException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
import time
import random
import pyperclip


options = webdriver.ChromeOptions()

options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36")
options.add_argument("--start-maximized")
###

class kreamStorage:
    def login(self):
        driver.find_element(By.XPATH, "//*[@id='__layout']/div/div[2]/div[1]/div/div[4]/button[1]").click()
        driver.implicitly_wait(2)
        # parent_window = driver.current_window_handle #부모 윈도우 값 저장
        # all_windows = driver.window_handles  #모든 윈도우 얻기
        # child_window = [window for window in all_windows if window != parent_window][0] # 자식 윈도우 얻기
        # driver.switch_to.window(child_window) # 윈도우 변경
        tabs = driver.window_handles
        driver.switch_to.window(tabs[1])
        driver.implicitly_wait(2)

        naver_id = 'lprince3'
        naver_pw = 'army960328*'
        pyperclip.copy(naver_id)
        driver.find_element(By.XPATH,'//*[@id="id"]').send_keys(Keys.CONTROL + 'v')
        pyperclip.copy(naver_pw)
        driver.find_element(By.XPATH,'//*[@id="pw"]').send_keys(Keys.CONTROL + 'v')
        time.sleep(0.7)
        driver.find_element(By.XPATH,'//*[@id="log.login"]').click()
        driver.implicitly_wait(1)
        driver.find_element(By.XPATH,'// *[ @ id = "new.save"]').click()
        time.sleep(2)
        driver.switch_to.window(tabs[0])

    def storeSell(self,product,my_size_text):
        total_cnt = random.randrange(20, 40)
        driver.get(f'https://kream.co.kr/products/{product}')
        driver.implicitly_wait(3)
        time.sleep(0.5)
        driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div[2]/div[1]/div/div[2]/div/div[1]/div[3]/div/a[2]').click() # 판매하기 클릭
        time.sleep(0.3)
        driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div[2]/div/div/div/div[2]/div/ul/li[3]/button').click() # 사이즈
        driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div[2]/div/div/div/div[2]/div[2]/a[1]').click() #보관신청
        flag = self.checkBox()
        driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/div/div/div/div[2]/div/a').click()  # 보관하기 버튼 클릭
        driver.implicitly_wait(1)


        # '//*[@id="__layout"]/div/div[2]/div/div/div/div[3]/div[1]' #S
        # '//*[@id="__layout"]/div/div[2]/div/div/div/div[3]/div[2]' #M
        # '//*[@id="__layout"]/div/div[2]/div/div/div/div[3]/div[3]' #L

        if my_size_text == '':
            driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/div/div/div/div[3]/div/div[2]/div/button[2]').click()  # 플스의 경우 개수 한번 클릭
        else:
            whichSize = driver.find_elements(By.CSS_SELECTOR,'div.inventory_size_item')
            for size in whichSize:
                if my_size_text == size.find_element(By.CLASS_NAME,'size').text:
                    my_size = size
                else:
                    continue
            my_size.find_elements(By.TAG_NAME, 'button')[1].click()  # 내 사이즈 증량 클릭

        while(flag):
            time.sleep(0.5)
            try:
                driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div[2]/div/div/div/div[4]/a').click()
                driver.implicitly_wait(1)
                time.sleep(random.randrange(1,3))
                da = Alert(driver)
                da.accept() # 팝업창 '확인' 클릭
            except NoSuchElementException:
                continue
            except NoAlertPresentException:
                flag = 0
                continue
# 두번째 관문
        flag = self.checkBox()

        while(flag):
            time.sleep(1.1)
            #try:
            da = Alert(driver)
            if da is None:
                driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/div/div/div/div[1]/section[6]/div[2]/a').click()  # 마지막 최종 결제
            else:
                da.accept()  # 팝업창 '확인' 클릭
            driver.implicitly_wait(1)

            # except UnexpectedAlertPresentException:
            #     try:
            #         da = Alert(driver)
            #         da.accept()
            #     except NoAlertPresentException:
            #         flag = 0
            #         driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div[2]/div/div/div/div[1]/section[6]/div[2]/a').click()
            #         continue
            #
            # except NoAlertPresentException:
            #     flag = 0
            #     continue





    def checkBox(self):
        flag = 1
        time.sleep(2)
        checkList = driver.find_element(By.CSS_SELECTOR, 'ul.check_list.lg')  #  체크리스트
        checks = checkList.find_elements(By.TAG_NAME, 'li')
        for check in checks:
            checkbox = check.find_element(By.TAG_NAME, 'svg')
            checkbox.click()
            time.sleep(0.2)
        time.sleep(1)
        return flag



driver = webdriver.Chrome('chromedriver.exe', options=options)
driver.get('https://kream.co.kr/login')
driver.implicitly_wait(3)

storage = kreamStorage()
storage.login()
#TODO 클래스 구현으로 깔끔하게 https://wikidocs.net/28
#ps5.storeSell('32974','')
storage.storeSell('50888','L') # 뒤에 사이즈 없으면 없는대로 작동
