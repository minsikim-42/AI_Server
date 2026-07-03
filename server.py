from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from services import ollama
from models import ChatRequest

app = FastAPI()

# HTML/CSS/JS 설정
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request,
        "index.html",
        {}
    )


@app.post("/chat")
def chat(request: ChatRequest):
    return StreamingResponse(
        ollama.chat(request),
        media_type="text/plain"
	)
