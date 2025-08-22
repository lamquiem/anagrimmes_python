from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from .database import get_db
from .crud import search_prononciation

app = FastAPI()
templates = Jinja2Templates(directory="api/templates")
app.mount("/static", StaticFiles(directory="api/static"), name="static")

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("chercher_prononciation.html", {
        "request": request,
        "results": [],
        "query": ""
    })

@app.post("/chercher_prononciation")
async def chercher_prononciation(request: Request, prononciation: str = Form(...)):
    db = get_db()
    results = search_prononciation(db, prononciation)
    return templates.TemplateResponse("chercher_prononciation.html", {
        "request": request,
        "results": results,
        "query": prononciation
    })
