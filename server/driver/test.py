from auth import get_driver
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
import logging
from webdriver_manager.chrome import ChromeDriverManager

driver= get_driver()
driver.maximize_window()
url='https://www.amazon.in/'
driver.get(url)
url= 'https://www.amazon.in/mobile'
driver.get(url)
# a-size-base-plus a-color-base a-text-normal
time.sleep(3)
# username=driver.find_elements('a-size-base-plus a-color-base a-text-normal')
print('next')
# driver.find_elements_by_class_name('a-size-base-plus a-color-base a-text-normal')
# username1=driver.find_elements(By.CLASS_NAME, 'a-size-base-plus a-color-base a-text-normal')
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)
username=driver.find_elements(By.CSS_SELECTOR, "span.a-size-base-plus.a-color-base.a-text-normal")
for j in range(len(username)):
    print(username[j].text)
time.sleep(10)
driver.close()