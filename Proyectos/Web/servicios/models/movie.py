from config.database import Base
from sqlalchemy import *

class Movie(Base):

    __tablename__ = "movies"
    id = Column(Integer, primary_key = True)
    title = Column(String)
    overview = Column(String)
    year = Column(Integer)
    rating = Column(Float)
    ratng = Column(String)
    category = Column(String)