import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session

load_dotenv()
engine = create_engine(os.environ["DATABASE_URL"])

class Base(DeclarativeBase):
    pass

# TODO: fungsi get_db() yang membuka Session(engine) dan yield
