#################
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware

from data.data import all_data

TITLE = "CDN - Fast & Local"
DESCRIPTION = "Serving CSS, JS, and other files quickly and locally for easy development."

# Define the App
app = FastAPI( title=TITLE, description=DESCRIPTION )
#Allows for HTML Response
templates = Jinja2Templates(directory="templates")
#Allows for static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# CORS Rules
origins = ["*"]

app.add_middleware( CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"] )

@app.get("/", response_class=HTMLResponse)
async def index(request: Request, id: int=None):
    return templates.TemplateResponse("index.html", { "request": request, "id": id, 'title': TITLE, "all_data": all_data })
