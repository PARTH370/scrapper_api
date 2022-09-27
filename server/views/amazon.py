from lib2to3.pgen2 import driver
from re import U
from server.driver.auth import *
from fastapi import APIRouter, Body
from server.models.amazon import serach
from fastapi.encoders import jsonable_encoder
import time
from selenium.webdriver.common.by import By
router = APIRouter()


@router.post("/", response_description="Add Body Part")
async def amazon(schema: serach = Body(...)):
    schema = jsonable_encoder(schema)
    driver= get_driver()
    # url='https://www.amazon.in/'
    # driver.get(url)
    url= 'https://www.amazon.in/s?k='+schema['item'].lower()
    driver.get(url)
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    data=[]
    time.sleep(2)
    print("0"*90)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # span.a-size-base.a-color-base.a-text-normal
    # h2.a-size-mini.a-spacing-none.a-color-base.s-line-clamp-2
    description=driver.find_elements(By.CSS_SELECTOR, "h2.a-size-mini.a-spacing-none.a-color-base.s-line-clamp-2")
    description12=driver.find_elements(By.CSS_SELECTOR, "span.a-size-base.a-color-base.a-text-normal")
    print("0"*90,len(description),len(description12))
    price=driver.find_elements(By.CSS_SELECTOR, "span.a-price-whole")
    # print(len(price),price)
    for j in range(min(len(description),len(price))):
        temp={}
        temp["Product"] = description[j].text
        temp["Price"] = price[j].text
        data.append(temp)
    driver.close()
    return {"username": data}

