# Prueba de despliegue automático CI/CD desde GitHub
# Prueba de despliegue automático CI/CD desde GitHub
# Prueba de despliegue automático CI/CD desde GitHub
# Prueba de despliegue automático CI/CD desde GitHub
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
import pickle
import pandas as pd
import uvicorn


# Cargar modelo y columnas
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("features.pkl", "rb") as f:
    feature_columns = pickle.load(f)

# Crear la app
app = FastAPI(title="Prediccion del Peso del Pez: ")

# Definir el esquema de entrada con Pydantic
class FishFeatures(BaseModel):
    Category: str
    Height: float
    Width: float
    Length1: float
    Length2: float
    Length3: float
# Prueba de despliegue automático CI/CD desde GitHub
# Prueba de despliegue automático CI/CD desde GitHub

@app.get("/")
async def root():
    return {"message": "Prueba de despliegue automático CI/CD desde GitHub!V3"}


@app.post("/predic/")
async def predict(data: FishFeatures):

#@app.get("/prediccion")
#async def predict(data: FishFeatures):

    try:
        # Convertir a DataFrame
        input_df = pd.DataFrame([data.dict()])

        # One-hot encoding + reordenar
        input_df = pd.get_dummies(input_df)
        input_df = input_df.reindex(columns=feature_columns, fill_value=0)
        # Predicción
        prediccion = model.predict(input_df)
        prediction = model.predict(input_df)[0]
        resultado = {
            "El peso estimado del pez es de: " : float(prediccion[0])
        }
        return resultado
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
