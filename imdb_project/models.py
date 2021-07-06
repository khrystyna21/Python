
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+pymysql://root:root-root21@localhost/imdb')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Movie(Base):
    __tablename__ = "movies"

    movie_id = Column(Integer, primary_key=True)
    movie_name = Column(String)
    movie_year = Column(Integer)
    duration = Column(Integer)
    imdb_rating = Column(Float)
    metascore = Column(Float)
    votes = Column(Integer)
    revenue = Column(Integer)
    movie_description = Column(String)
    director = Column(String)


for movie in session.query(Movie.director).filter(Movie.movie_name.like('Titanic')):
    print(movie)





