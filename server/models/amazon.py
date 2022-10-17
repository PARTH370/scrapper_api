from typing import List, Optional
from pydantic import BaseModel, HttpUrl


class serach(BaseModel):
    item: str

    class Config:
        schema_extra = {"example": {"item":"Enter The Detail you want to scrape"}}


class url(BaseModel):
    url= str
    class  Config:
        schema_extra = {"example": {"url":"http://example.com/scrape"}}

def responses(data):
    return {
        'code': 200,
        'data': data,
        'msg': 'Data was successfully retrieved'
    }