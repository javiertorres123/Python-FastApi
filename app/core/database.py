from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()  # Carga el archivo .env automáticamente

DATABASE_URL = os.getenv("DATABASE_URL")

# SQLAlchemy: conexión al motor
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True  # Repara conexiones rotas automáticamente
)

# Sesiones
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base modelo
Base = declarative_base()

# Dependencia para obtener sesión
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
