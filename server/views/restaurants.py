from server.driver.auth import get_driver , Keys
from fastapi import APIRouter
import time
from selenium.webdriver.common.by import By
router = APIRouter()


@router.post("/", response_description="Get Near Restaurants list")
async def restaurants():
    driver= get_driver()
    url= 'https://www.google.com/'
    driver.get(url)
    x=driver.find_element(By.CSS_SELECTOR,'input.gLFyf.gsfi')
    x.send_keys('restaurants near me')
    x.send_keys(Keys.ENTER)
    data=[]
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR,'span.wUrVib.OSrXXb').click()
    name = driver.find_elements(By.CSS_SELECTOR,'span.OSrXXb')
    rating = driver.find_elements(By.CSS_SELECTOR , 'span.YDIN4c.YrbPuc')
    time.sleep(2)
    length=min(len(name),len(rating))
    for j in range(3,length):
        temp={}
        temp["Restaurant_Name"] = name[j].text
        try:
            temp["Rating"] = rating[j+4].text
        except:
            break
        print(data)
        data.append(temp)
    driver.close()
    return {"username": data}
