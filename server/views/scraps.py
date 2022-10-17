from server.driver.auth import get_driver , Keys
from fastapi import APIRouter , Body
from fastapi.encoders import jsonable_encoder
from server.models.amazon import url, responses
from selenium.webdriver.common.by import By

router = APIRouter()


@router.post("/", response_description="Get Near Restaurants list")
async def restaurants(schema: url = Body(...)):
    driver= get_driver()
    schema = jsonable_encoder(schema)
    driver.get(schema['url'])
    
