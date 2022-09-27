
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
# from selenium import BASE_DIR
import os
BASE_DIR = os.path.dirname(__file__)
CHROME_PATH = BASE_DIR + "/chromedriver"

import os
BASE_DIR = os.getcwd()
print(BASE_DIR)
from webdriver_manager.chrome import ChromeDriverManager
def get_driver():
    options = Options()
    
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    browser = webdriver.Chrome( executable_path=CHROME_PATH,chrome_options=options)
    return browser


