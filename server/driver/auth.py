
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
import logging
from webdriver_manager.chrome import ChromeDriverManager
def get_driver():
    options = Options()
    
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    browser = webdriver.Chrome( ChromeDriverManager().install(),chrome_options=options)
    return browser


