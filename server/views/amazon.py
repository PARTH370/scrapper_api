from server.driver.auth import get_driver
from fastapi import APIRouter, Body
from server.models.amazon import serach, responses
from fastapi.encoders import jsonable_encoder
import time
from selenium.webdriver.common.by import By
router = APIRouter()


@router.post("/", response_description="Get search results from Amazon")
async def amazon(schema: serach = Body(...)):
    """ 
        Summary line. 
        This function gathers data from  amazon for user choice 

        Parameters: 
        request :  contains dictionary called as test various checked row parameter in form of key and value

        Returns: 
        scrape data in form of key and value 

    """
    schema = jsonable_encoder(schema)
    driver = get_driver()
    url = 'https://www.amazon.in/s?k='+schema['item'].lower()
    driver.get(url)
    data = []
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    description = driver.find_elements(
        By.CSS_SELECTOR, "h2.a-size-mini.a-spacing-none.a-color-base.s-line-clamp-2")
    price = driver.find_elements(By.CSS_SELECTOR, "span.a-price-whole")
    for j in range(min(len(description), len(price))):
        temp = {}
        temp["Product"] = description[j].text
        temp["Price"] = price[j].text
        data.append(temp)
    driver.close()
    return responses(data)
