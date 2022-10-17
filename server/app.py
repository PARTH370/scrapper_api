from fastapi import FastAPI, Response ,Request
import uvicorn
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from server.views.amazon import router as amazon
from server.views.flipkart import router as flipkart
from server.views.news import router as news
from server.views.restaurants import router as restaurants
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from server.views.city import router as city


app = FastAPI()
app.mount("/Templetes", StaticFiles(directory="server/Templetes"), name="Templetes")
templates = Jinja2Templates(directory="server/Templetes")
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
app.include_router(restaurants, tags=["restaurants"], prefix="/restaurants")
app.include_router(city, tags=["city"], prefix="/city")

@app.get("/items", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse(
        "base.html",
        {"request": request}
    )


@app.get('/')
def home():
    return {"Welcome": "Web Scraper"}
        