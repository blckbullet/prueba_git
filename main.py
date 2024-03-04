from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware




app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir solicitudes desde cualquier origen, puedes ajustar esto según tus necesidades
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],  # Permitir estos métodos HTTP
    allow_headers=["*"],  # Permitir todos los encabezados en las solicitudes
)


@app.get("/{precio}/")
def calcular(precio:int):
    return {"resultado": precio + (precio * 0.16)}
