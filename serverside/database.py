from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
# from psycopg2.extras import RealDictCursor
# import time
from config import Settings
settings = Settings()

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

# conn_string = f"host='http://hackman.cdlfs0pqljpt.eu-north-1.rds.amazonaws.com' dbname='hackman' user='shivansh' password='Masterpass1.'"
# engine = psycopg2.connect(dbname='postgres', user='shivansh', password='Masterpass1.', host='hackman.cdlfs0pqljpt.eu-north-1.rds.amazonaws.com')
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
