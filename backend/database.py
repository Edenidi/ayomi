from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL de la base de données SQLite
SQLALCHEMY_DATABASE_URL = "sqlite:///./app.db"

# Créer le moteur de la base de données
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Créer la session de la base de données
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Déclarer la base pour définir les modèles
Base = declarative_base()

# Modèle pour stocker les calculs
class Calculation(Base):
    __tablename__ = "calculations"

    id = Column(Integer, primary_key=True, index=True)
    expression = Column(String, index=True)
    result = Column(Float)

# Créer les tables dans la base de données
def init_db():
    Base.metadata.create_all(bind=engine)
