
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
import os
from webdriver_manager.chrome import ChromeDriverManager
def get_driver():
    options = Options()
    options = Options()
    options.add_argument("--headless")
    options.binary_location = os.environ.get('GOOGLE_CHROME_BIN')
    options.add_argument("--no-sandbox")
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    # browser = webdriver.Chrome( ChromeDriverManager().install(),chrome_options=options)
    return webdriver.Chrome(executable_path=str(os.environ.get('CHROMEDRIVER_PATH')), chrome_options=options)


