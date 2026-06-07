from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.model import generate_response

app = FastAPI(title="GenAI Assistant")

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(
    directory="templates"
)

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )

@app.post("/generate")
async def generate(payload: dict):
    message = payload.get("message")
    model = payload.get("model")

    if not message or not model:
            raise HTTPException(status_code=400, detail="Missing message or model selection")

    try:
        result = generate_response(user_message=message, model_name=model)
        return JSONResponse(content=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
