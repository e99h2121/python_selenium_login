#!python3.8

import time
import chromedriver_binary

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# https://selenium-python.readthedocs.io/waits.html

url = "enter url"
elem_name_inp_uid = "user_id etc"
elem_val_inp_uid = "enter user_id"
elem_name_inp_pwd = "password etc"
elem_val_inp_pwd = "enter password"
elem_name_btn_login = "login-syussya-button etc"

driver = webdriver.Chrome()
driver.get(url)

elem_inp_uid = driver.find_element_by_name(elem_name_inp_uid) 
elem_inp_uid.clear()
elem_inp_uid.send_keys(elem_val_inp_uid)
elem_inp_pwd = driver.find_element_by_name(elem_name_inp_pwd)
elem_inp_pwd.clear()
elem_inp_pwd.send_keys(elem_val_inp_pwd)
elem_btn_logout = driver.find_element_by_class_name(elem_name_btn_login)
elem_btn_logout.click()

time.sleep(5)


