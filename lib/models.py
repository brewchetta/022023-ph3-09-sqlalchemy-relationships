from sqlalchemy import create_engine, func, Table
from sqlalchemy import ForeignKey, Table, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

movie_ticket = Table(
    'movie_tickets',
    Base.metadata,
    Column('movie_id', ForeignKey('movies.id'), primary_key=True),
    Column('moviegoer_id', ForeignKey('moviegoers.id'), primary_key=True),
    Column('price', Integer()),
    extend_existing=True,
)

# MOVIE ---< ROLES
# one to many

# ACTOR ---< ROLES
# one to many

# MOVIE >---< ACTOR
# many to many

# MOVIE ---< ROLES >--- ACTOR
# roles gets all the foreign keys


class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer(), primary_key=True)
    title = Column(String())

    roles = relationship('Role', back_populates='movie')
    actors = association_proxy('roles', 'actor', creator= lambda ac: Role(actor = ac))

    moviegoers = relationship('Moviegoer', secondary=movie_ticket, back_populates='movies')

    def __repr__(self):
        return f'<Movie(id={self.id} title={self.title})>'

class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer(), primary_key=True)
    character_name = Column(String())

    movie_id = Column(Integer(), ForeignKey('movies.id'))
    actor_id = Column(Integer(), ForeignKey('actors.id'))

    movie = relationship('Movie', back_populates='roles')
    actor = relationship('Actor', back_populates='roles')

    def __repr__(self):
        return f'<Role(id={self.id} character_name={self.character_name} movie_id={self.movie_id} actor_id={self.actor_id})>'

class Actor(Base):
    __tablename__ = 'actors'

    id = Column(Integer(), primary_key = True)
    name = Column(String())

    roles = relationship('Role', back_populates = 'actor')
    movies = association_proxy('roles', 'movie', creator= lambda mv: Role(movie = mv))

    def __repr__(self):
        return f'<Actor(id={self.id} name={self.name})'

class Moviegoer(Base):
    __tablename__ = 'moviegoers'

    id = Column(Integer(), primary_key = True)
    name = Column(String())

    movies = relationship('Movie', secondary=movie_ticket, back_populates='moviegoers')

    def __repr__(self):
        return f'<Moviegoer(id={self.id} name={self.name})'
