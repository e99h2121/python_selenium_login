import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = ""
elem_name_inp_uid = ""
elem_val_inp_uid = ""
elem_name_inp_pwd = ""
elem_val_inp_pwd = ""
elem_name_btn_login = ""

driver = webdriver.Chrome()
driver.get(url)
elem_inp_uid = driver.find_element_by_name(elem_name_inp_uid) 
elem_inp_uid.clear()
elem_inp_uid.send_keys(elem_val_inp_uid)
elem_inp_pwd = driver.find_element_by_name(elem_name_inp_pwd)
elem_inp_pwd.clear()
elem_inp_pwd.send_keys(elem_val_inp_pwd)
elem_btn_login = driver.find_element_by_name(elem_name_btn_login)
elem_btn_login.click()
time.sleep(5)

driver.close()
