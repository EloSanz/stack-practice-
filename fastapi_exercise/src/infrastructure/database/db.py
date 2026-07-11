from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Connection details matching the docker-compose.yml configuration
DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/fastapi_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
