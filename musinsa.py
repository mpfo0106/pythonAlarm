from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pyautogui as pg
import random

options = webdriver.ChromeOptions()

options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36")
options.add_argument("--start-maximized")


driver = webdriver.Chrome('chromedriver.exe', options=options)
driver.get('https://adcr.naver.com/adcr?x=FslHCiLYwjHDiajwuP3y4f///w==koEYRT4uIN9V3muAnu8FUno5JCddFs8e9LLWlzVGiGWA24jRoPffD5BBUuBnSUAsUE+iipUTAvVJ4B/StXDxaxI0oMeMJmp2YUhlCiC5Rl6oxAsJ7J7QcGe9X6ExCWrAUDfKhrg/1kNux1XeiER7nUim+Mgl6RzFUOkiIGzXTksiG2qdJqVNXhmsUl7I0r86sG3cmyDas3gXaBo/abmq+nXD02/FWCTzw0xbWOJoVqYvEB2aghOxvXP0CQ2d1Yd0XEQRJb/x3UzzvyN5SEXelU0Fh07QF6AsUdwDPuKFaC6OdEFZtgJNa+COqhWbJsq8oC99gfC/m6QVk8DEUYUuDZOosYRQASRhnb3rEs5RqlRl4iRYqi/e5Qdp86PI6vhf/VQt4t6swGIc24lAcrL3quSwy/z/9LK2yY+GP3YDbLzWU91EF6qIv90aHJMNUm5WiwGEPfty420Zho6etSkV+18QNVMUCukRsQeP4ZMNMq13cKAdrprHXYs9EFddfpAXQtnTxQEcV7XsYo1EVowfyuICkak2izIRMQfIo7oAwo6VC4Y7tCifQ+v33OSTPAMsKoW3OLRRh8M+8wnczvSGIE4ciLq+VlkbbXWR7Z2jCz8ANnMmOpOKYKn8aWFxdPzLKJypbjrCfD8gTqEUM7PXIxIZJBYycdPMha5D14xVammqE1Ez8z9wtEiW+k1utXAq7bdW8Xf8IJOIcsaUt85PrX7XR6Umyer5kvdElcRmc4BhYNXyldNoOQ4bFXi2rKDLT+0X9kKxTB+dMaRHzyN8kIOE2lcafhYmkeESIZTMTd2+hSuGfKDBOYy/EqLn6bZ0qAirilJ24JD/KnLfAo9V2ulLaci6HLWOorIRxe3jDEza/gbsFy/1g27AwT3V8d6PHMle3FmVrkDIy55dByjbYdmq8ZqQHAHUUDuz3oI2hir7xz/+z94MzIK8PFJy50rGjO6Y+szyivI5a9t1ClxP/4w==&p=0')


driver.implicitly_wait(5)
id = 'mpfo551'
pw = 'joonho7878'

def login(id,pw):
    btn = driver.find_element(By.XPATH, '//*[@id="default_top"]/div[3]/button')
    btn.click()

    idBox = driver.find_element(By.XPATH, '/html/body/div[1]/section/div[1]/form/div[1]/div[1]/div/input')
    idBox.click()
    idBox.send_keys(id)
    time.sleep(0.5)
    pwBox = driver.find_element(By.XPATH, '/html/body/div[1]/section/div[1]/form/div[1]/div[2]/div/input')
    pwBox.click()
    pwBox.send_keys(pw)
    time.sleep(0.5)
    pwBox.send_keys(Keys.ENTER)
    time.sleep(4)

def purchase():
    productUrl = 'https://www.musinsa.com/app/goods/2545496/0'
    driver.get(productUrl)
    i = 1
    select_box = driver.find_element(By.XPATH,'//*[@id="option1"]')
    sizes = select_box.find_elements(By.TAG_NAME,'option')

    jaego = select_box.find_elements(By.TAG_NAME,'jaego_yn')
    while True:
        if sizes[len(sizes) -i].get_attribute('jaego_yn') == 'Y':
            sizes[len(sizes) -i].click()
            break
        else:
            i += 1

    buy_btn = driver.find_element(By.XPATH,'//*[@id="buy_option_area"]/div[7]/div[1]/a')
    buy_btn.click()
    driver.implicitly_wait(0.5)

    prepointUse = driver.find_element(By.CSS_SELECTOR,'input#prepointUse')
    prepointUse.click()
    pointUse = driver.find_element(By.CSS_SELECTOR,'input#pointUse')
    pointUse.click()

    #driver.switch_to.frame('payment_result')
    payment = driver.find_element(By.XPATH,'//*[@id="__payment-choice-view"]')
    musinsaPay = payment.find_element(By.XPATH,'//label[text() = "무신사페이"]')
    musinsaPay.click()
    driver.implicitly_wait(0.4)

    # naver_pay = driver.find_element(By.XPATH,'//*[@id="payment_info_area"]/div[4]/ul/li[2]/div[1]/label[8]') #네이버 페이
    # naver_pay.click()
    # time.sleep(1)

    checkOut = driver.find_element(By.XPATH,'//*[@id="btn_pay"]')
    checkOut.click()



def musinsaPayPw(): #pyautogui 이용함. 성능이 구리면 opencv 도 이용할 예정
    # TODO 여기서 막힘ㅜ + 시간 땡 하면 결제 되는 시스템으로
    driver.switch_to.window(driver.window_handles[1])  # 결제창 전환
    driver.implicitly_wait(1)
    button0 = pg.locateOnScreen('C:/Code/python/pythonMacro/img/0.png',confidence =0.7)
    time.sleep(2)
    button1 = pg.locateOnScreen('C:/Code/python/pythonMacro/img/1.png', confidence =0.7)
    time.sleep(2)
    button2 = pg.locateOnScreen('C:/Code/python/pythonMacro/img/2.png', confidence =0.7)
    time.sleep(2)
    print(button0)
    print(button1)
    print(button2)

    #
    # pg.moveTo(button0)
    # pg.doubleClick()
    # time.sleep(1)
    #
    # pg.moveTo(button1)
    # pg.doubleClick()
    # time.sleep(1)
    #
    # pg.moveTo(button2)
    # pg.doubleClick()
    # time.sleep(1)




    # size = len(sizes)-1
    # if jaego[size] =="Y":
    #     sizes[size].click()
    # else:
    #     size -= 1



login(id,pw)
purchase()
musinsaPayPw()