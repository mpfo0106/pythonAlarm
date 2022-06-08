import random
import re
import requests
from bs4 import BeautifulSoup
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"}
##########
def create_soup(url):
    res = requests.get(url, headers= headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup

url = "https://www.nike.com/kr/ko_kr/t/men/fw/nike-sportswear/CW2288-111/avbt44/air-force-1-07"

soup = create_soup(url)

shoes = soup.find_all("span",attrs={"class":"input-radio"})
# print(shoes[0].find("label").get_text())
for shoe in shoes:
    soldOut = shoe.find("input", attrs={"disabled":"disabled"})
    print(soldOut)

