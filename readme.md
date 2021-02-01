
# Automate your work:Attendance Punch-in

### set up python and vscode
https://docs.microsoft.com/ja-jp/learn/modules/python-install-vscode/


### Selenium Python installation
https://selenium-python.readthedocs.io/installation.html

1.2

`python -m pip install selenium`

or

`python3 -m pip install selenium`

1.3

mac

```
brew update 
brew install chromedriver
```

windows

`python -m pip install chromedriver-binary-auto`

or 

https://www.mittsu-kosen.com/chromedriver%E3%82%92windows10%E3%81%A7%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95%E3%80%90%E7%94%BB%E5%83%8F%E4%BB%98%E3%81%8D%E3%80%91/

1.5 and 1.6 is not needed

###  create and execute sample code

python_org_search.py

```
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import chromedriver_binary # for pip install chromedriver-binary-auto if you use mac insatll above

driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q") 
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
```

`python3 python_org_search.py`

Mac

if security confirmation shows, allow it from System Preference

### create login script for your attendance  system

login.py

```
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import chromedriver_binary # for pip install chromedriver-binary-auto if you use mac insatll above

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

```

### if you do not want to close the browser

```
import os
import signal
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import chromedriver_binary # for pip install chromedriver-binary-auto if you use mac insatll above

try:
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
    
finally:
    os.kill(driver.service.process.pid,signal.SIGTERM) 

```

if it does not have id for button

```
elems_btns = driver.find_elements_by_class_name("")
elems_btns[0].click();

```

if it need javascript

```
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
```
