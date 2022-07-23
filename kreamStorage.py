from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException, UnexpectedAlertPresentException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
import time
import random
import pyperclip
import chromedriver_autoinstaller
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
# options.headless = True
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36")
options.add_argument("--start-maximized")
###

class kreamStorage:
    def login(self):
        driver.find_element(By.XPATH, "//*[@id='__layout']/div/div[2]/div[1]/div/div[4]/button[1]").click()
        driver.implicitly_wait(2)
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


    def storeSell(self,product,my_size):
        cnt =0
        driver.get(f'https://kream.co.kr/products/{product}')
        driver.implicitly_wait(3)
        time.sleep(0.5)
        driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div[2]/div[1]/div/div[2]/div/div[1]/div[3]/div/a[2]').send_keys(Keys.ENTER) # 판매하기 클릭
        time.sleep(0.7)

        if my_size != '': #사이즈가 있는경우, 없으면 바로 보판 클릭임
            sizeBtn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,f'//span[contains(text(),"{my_size}")]//ancestor :: button')))
            #sizeBtn = driver.find_element(By.XPATH, f'//span[contains(text(),"{my_size}")]//ancestor :: button') #TODO A1 사이즈 변경
            time.sleep(0.7)
            sizeBtn.click()
        bopan =driver.find_element(By.CSS_SELECTOR,'a.btn_order.order_sell.inventory_ask.clickable') #보관신청
        bopan.click()


        flag = self.checkBox()## 체크박스 클릭
        nextBtn = driver.find_element(By.XPATH, '//*[contains(text(),"다음")]')
        nextBtn.send_keys(Keys.ENTER)

        # 개수 증량선택
        if my_size == '':
            driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/div/div/div/div[3]/div/div[2]/div/button[2]').click()  # 플스의 경우 개수 한번 클릭
        else:
            my_size_div = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,f'//div[contains(text(),"{my_size}")]//parent :: div')))
            #my_size_div = driver.find_element(By.XPATH,f'//div[contains(text(),"{my_size}")]//parent :: div') #TODO A1 사이즈로 바꿔
            my_size_plus_btn = my_size_div.find_elements(By.TAG_NAME,'button')[1]
            time.sleep(0.5)
            my_size_plus_btn.click()


        #TODO 1) 보판 경고문 발생!!
        while(flag):
            time.sleep(0.7)
            try:
                application_next = driver.find_element(By.XPATH,'//*[contains(text(), "신청 계속")]')
                application_next.send_keys(Keys.ENTER)

                driver.implicitly_wait(2)
                # 경고문 안뜨면
                titlePage = driver.find_element(By.CSS_SELECTOR,'span.title_txt').text
                if titlePage == "신청 내역":
                    break

                #경고문 뜨면
                time.sleep(3)
                da = Alert(driver)
                time.sleep(1)
                da.accept() # 팝업창 '확인' 클릭

                cnt +=1
                if cnt>1000:
                    driver.refresh()
                    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,f'//div[contains(text(),"{my_size}")]//parent :: div')))
                    my_size_plus_btn.click()
                    cnt =0
            except NoSuchElementException:
                continue
            except NoAlertPresentException:
                flag = 0
                continue

#TODO 2) 두번째 관문
        driver.implicitly_wait(2)
        flag = self.checkBox()
        checkOut_btn = driver.find_element(By.XPATH, '//*[contains(text(),"결제하기")]')
        checkOut_btn.send_keys(Keys.ENTER)
        #경고문이 뜨면
        while(flag):
            time.sleep(3)
            da = Alert(driver)
            # # 경고문이 안뜨면
            # if da is None:
            #     time.sleep(1)
            #     checkOut_btn.click()  # 마지막 최종 결제
            # 경고문이 뜨면
            time.sleep(1)
            da.accept() #팝업창 확인 클릭
            driver.implicitly_wait(1)
            checkOut_btn.send_keys(Keys.ENTER)


    def checkBox(self):
        flag = 1
        checkList = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'ul.check_list.lg')))
        #checkList = driver.find_element(By.CSS_SELECTOR, 'ul.check_list.lg')  #  체크리스트
        time.sleep(1)
        checks = checkList.find_elements(By.TAG_NAME, 'li')
        for check in checks:
            checkbox = check.find_element(By.TAG_NAME, 'svg')
            checkbox.click()
            time.sleep(0.2)
        time.sleep(1)
        return flag



chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]  # 크롬드라이버 버전 확인
try:
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe',options=options)
except:
    chromedriver_autoinstaller.install(True)
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe',options=options)
# driver = webdriver.Chrome('chromedriver.exe', options=options)
driver.get('https://kream.co.kr/login')
driver.implicitly_wait(3)

storage = kreamStorage()
storage.login()
storage.storeSell('65117','A1')
# storage.storeSell('12831','275')
