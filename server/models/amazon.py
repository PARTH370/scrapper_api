from typing import List, Optional
from pydantic import BaseModel, HttpUrl


class serach(BaseModel):
    item: str

    class Config:
        schema_extra = {"example": {"item":"Enter The Detail you want to scrape"}}
