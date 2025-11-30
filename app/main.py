from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db

app = FastAPI(title="Sistema de Inventario")

@app.get("/check-db")
def check_db(db: Session = Depends(get_db)):
    return {"status": "Conexión OK"}