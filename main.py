from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel


app = FastAPI()
templates = Jinja2Templates(directory="templates")  
app.mount("/static", StaticFiles(directory="static"), name="static")

class InputData(BaseModel):
    precio: float

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/calcular")
async def calcular(input_data: InputData):
    precio = input_data.precio
    # Aquí podrías realizar el cálculo necesario
    resultado = precio + (precio * 0.16)
    return JSONResponse(content={"resultado": resultado})
