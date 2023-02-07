from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

#'postgresql+psycopg2://user:password@hostname/database_name'
engine = create_engine("postgresql+pyscopg2://raiane:banco123@hostname/dbname")