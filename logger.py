import selenium
import time
#import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import Secret 

url_login="https://net.du.ac.ir/login"
url_logged="https://net.du.ac.ir/status"
handeler =Secret.get_Password()
usrname, pw = handeler[0], handeler[1]; del handeler

options = Options()
options.add_argument("--headless")
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=options)

driver.get(url_login)

while(True):
    driver.get(url_login)
    time.sleep(5)
    if (driver.current_url == url_login):
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys(usrname)

        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys(pw)
        driver.find_element_by_css_selector("input[type=submit]").click()
    
    time.sleep(wait)