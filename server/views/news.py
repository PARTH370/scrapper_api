from server.driver.auth import *
from fastapi import APIRouter, Body
from server.models.amazon import serach
from fastapi.encoders import jsonable_encoder
import time
from selenium.webdriver.common.by import By
router = APIRouter()


@router.post("/", response_description="Add Body Part")
async def news():
    # schema = jsonable_encoder(schema)
    driver= get_driver()
    url= 'https://www.news18.com/topics/showsha-exclusives/'
    driver.get(url)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    data=[]
    # time.sleep(8)
    img_url=driver.find_elements(By.CSS_SELECTOR, "img.jsx-470016334.lazyloaded")
    headline=driver.find_elements(By.CSS_SELECTOR, "p.jsx-470016334")
    for j in range(min(len(img_url),len(headline))):
        temp={}
        temp["Product"] = img_url[j].get_attribute('src')
        temp["Price"] = headline[j].text
        data.append(temp)
        # temp["Price"] = price[j].text
    driver.close()
    return {"username": data}
