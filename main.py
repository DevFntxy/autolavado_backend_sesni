from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI(title="Mi API de Saludo")  # Puedes ponerle un título opcional

# Redirigir la raíz "/" a "/docs"
@app.get("/", include_in_schema=False)  # no aparece en la documentación
def root():
    return RedirectResponse(url="/docs")

# Ruta de saludo
@app.get("/saludo", tags=["Saludo"])
def saludo():
    """
    Retorna un mensaje de saludo.
    """
    return {"message": "¡Hola, FastAPI!"}
