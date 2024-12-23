from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base


#Engine

engine = create_engine("sqlite:///store.db",echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

#make my session

def get_session():
    return Session()