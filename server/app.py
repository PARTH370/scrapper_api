from fastapi import FastAPI, Response
import uvicorn
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from server.views.amazon import router as amazon
from server.views.flipkart import router as flipkart
from server.views.news import router as news
app = FastAPI()
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(amazon, tags=["amazon"], prefix="/amazon")
app.include_router(flipkart, tags=["flipkart"], prefix="/flipkart")
app.include_router(news, tags=["news"], prefix="/news")
@app.get('/')
def home():
    return {"Welcome": "Web Scraper"}
        