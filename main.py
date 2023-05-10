from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup  # парсер
import account
import sbor_inf

import time
import random

option = webdriver.ChromeOptions()
option.add_argument('--ignore-certificate-errors')  # not to touch the site certificate
option.add_argument("--disable-blink-features=AutomationControlled")  # detour detect from fact
driver = webdriver.Chrome(
    executable_path="C:\chromedriver.exe",
    options=option
)

def main():
    login = account.login
    password = account.password
    driver.get('https://skycrypto.net')  # open site
    element = WebDriverWait(driver, 20).until(  # we wait a downloading site
        EC.element_to_be_clickable((By.CLASS_NAME, "top-nav__btn"))).click()  # search a button

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Войти"))).click()
    # click on sign up
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, "email"))).send_keys(login)
    #  add a login to email field
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, "password")))
    element.send_keys(password)  # add password in field password
    element.send_keys(Keys.ENTER)  # enter

    first_circle = True  # for determine a entrance in function
    nick_btc = '615nd'  # input('Input your nick in BTC: ')
    max_random_value = input('Input a random value: \n')
    num = input("Input a banks:\n"
                "1)Sberbank\n"
                "2)Tinkoff\n"
                "3)Card on Card\n"
                "4)All bank\n"
                "5)Mastercard\n"
                "6)Alpha\n"
                "7)Visa\n")
    banks_list = []
    for element in num:
        if element == '1':  # sberbank
            banks_list.append(2)
        if element == '2':  # tinkoff
            banks_list.append(3)
        if element == '3':  # s kart na kartu
            banks_list.append(4)
        if element == '4':  # all bank
            banks_list.append(5)
        if element == '5':  # master
            banks_list.append(7)
        if element == '6':  # alpha
            banks_list.append(8)
        if element == '7':  # visa
            banks_list.append(10)

    for id_bank in banks_list:
        sbor_inf.sbor_inf(id_bank, max_random_value, first_circle, nick_btc)


if __name__ == '__main__':
    main()
