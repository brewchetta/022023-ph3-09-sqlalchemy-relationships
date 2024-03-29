from sqlalchemy import create_engine, func #, Table
from sqlalchemy import ForeignKey, Table, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.ext.associationproxy import association_proxy

metadata = MetaData()

Base = declarative_base(metadata=metadata)



# Movie ----< Role
# one to many relationship

# FOREIGN KEY --> Role (the many)



class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer(), primary_key=True)
    title = Column(String())
    year_released = Column(Integer())

    # roles = relationship('Role', backref=backref('movie'))
    roles = relationship('Role', back_populates='movie')

    def __repr__(self):
        return f'<Movie(id={self.id} title={self.title} number_of_roles={len(self.roles)})>'

class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer(), primary_key=True)
    character_name = Column(String())
    actor = Column(String())

    movie_id = Column(Integer(), ForeignKey('movies.id'))

    movie = relationship('Movie', back_populates='roles')

    def __repr__(self):
        return f'<Role(id={self.id} character_name={self.character_name} movie_id={self.movie_id})>'
