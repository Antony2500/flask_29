from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

engine = create_engine(f"postgresql+psycopg2://{PGUSER}:{PGPASSWORD}@localhost:5433/online_restaurant", echo=True)
Session = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass