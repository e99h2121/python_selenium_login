#!python3.8

import time
import chromedriver_binary

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

# https://selenium-python.readthedocs.io/waits.html

url = "enter url"
elem_name_inp_uid = "user_id etc"
elem_val_inp_uid = "enter user_id"
elem_name_inp_pwd = "password etc"
elem_val_inp_pwd = "enter password"
elem_name_btn_logout = "login-taisya-button etc"

# driver = webdriver.Chrome()
driver = webdriver.Chrome(ChromeDriverManager().install())

#open tab
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't') 
# You can use (Keys.COMMAND + 't') on other OSs

# Load a page 
# Getwild
driver.get('https://www.youtube.com/watch?v=NHKq8IOXPxA')
# うっせぇわ
# driver.get('https://www.youtube.com/watch?v=Qp3b-RXtz4w')

# 再生をする
driver.find_element_by_class_name('ytp-play-button').click()

# 広告をスキップしたいけど、広告が出ないこともあるしどうしよう。。
# https://github.com/1993jayant/youtube_adskipper/blob/master/youtube_adskipper.py
# https://github.com/douasin/youtube-ad-skipper/blob/master/youtube_ad_skipper.py
# https://stackoverflow.com/questions/62745175/how-to-click-the-skip-ads-button-in-youtube-using-selenium-in-python-3
# https://stackoverflow.com/questions/36503730/continue-the-script-if-an-element-is-not-found-using-selenium-in-python

for i in range(3):
    time.sleep(10)
    try:
        driver.find_element_by_class_name('ytp-ad-skip-button.ytp-button').click()
    except:
        print("except");

# 30秒間音楽をお楽しみ
time.sleep(30)

driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't') 
# You can use (Keys.COMMAND + 't') on other OSs

# Load a page 
driver.get(url)

elem_inp_uid = driver.find_element_by_name(elem_name_inp_uid) 
elem_inp_uid.clear()
elem_inp_uid.send_keys(elem_val_inp_uid)
elem_inp_pwd = driver.find_element_by_name(elem_name_inp_pwd)
elem_inp_pwd.clear()
elem_inp_pwd.send_keys(elem_val_inp_pwd)
elem_btn_logout = driver.find_element_by_class_name(elem_name_btn_logout)
elem_btn_logout.click()

time.sleep(5)


