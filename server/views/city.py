from calendar import c
from itertools import count
from server.driver.auth import get_driver , Keys
from fastapi import APIRouter
import time
from selenium.webdriver.common.by import By
router = APIRouter()

import json

@router.post("/", response_description="Get Near Restaurants list")
async def restaurants():
    driver= get_driver()
    data={}
    for i in range(1,90):
        url= 'https://geokeo.com/database/state/'+str(i)+'/'
        driver.get(url)
        state = driver.find_elements(By.XPATH, "/html/body/main/div/table[1]/tbody/tr/td[2]")
        country = driver.find_elements(By.XPATH , '/html/body/main/div/table[1]/tbody/tr/td[3]')
        for j in range(0,len(state)):
            states=state[j].text
            countrys= country[j].text
            print(states,countrys)
            data[states]=countrys
    
    json_object = json.dumps(data)
 
    # Writing to sample.json
    with open("counter_with_state.json", "w") as outfile:
        outfile.write(json_object)
    return data


@router.get('city/{state}')
def get_city(state):

    f = open('counter_with_state.json')
    
    # returns JSON object as 
    # a dictionary
    data = json.load(f)
    return data[state.capitalize()]
    
