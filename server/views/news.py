from server.driver.auth import get_driver
from fastapi import APIRouter
from server.models.amazon import responses
from selenium.webdriver.common.by import By
router = APIRouter()


@router.post("/", response_description="Get Letest News")
async def news():
    driver = get_driver()
    url = 'https://www.news18.com/topics/showsha-exclusives/'
    driver.get(url)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    data = []
    headline = driver.find_elements(By.CSS_SELECTOR, "p.jsx-470016334")
    for j in range(len(headline)):
        temp = {}
        temp["Headline"] = headline[j].text
        data.append(temp)
    driver.close()
    return responses(data)
