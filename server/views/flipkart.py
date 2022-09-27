




from server.driver.auth import *
from fastapi import APIRouter, Body
from server.models.amazon import serach
from fastapi.encoders import jsonable_encoder
import time
from selenium.webdriver.common.by import By
router = APIRouter()


@router.post("/", response_description="Add Body Part")
async def flipkart(schema: serach = Body(...)):
    schema = jsonable_encoder(schema)
    driver= get_driver()
    url= 'https://www.flipkart.com/search?q='+schema['item'].lower()
    driver.get(url)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    data=[]
    # time.sleep(8)
    description=driver.find_elements(By.CSS_SELECTOR, "div._4rR01T")
    price=driver.find_elements(By.CSS_SELECTOR, "div._30jeq3._1_WHN1")
    for j in range(min(len(description),len(price))):
        temp={}
        temp["Product"] = description[j].text
        temp["Price"] = price[j].text
        data.append(temp)
        # temp["Price"] = price[j].text
    driver.close()
    return {"username": data}
