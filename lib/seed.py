from faker import Faker
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Movie, Role

if __name__ == '__main__':
    engine = create_engine('sqlite:///many_to_many.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Role).delete()
    session.query(Movie).delete()

    fake = Faker()

    movies = []
    for i in range(50):
        movie = Movie(
            title=fake.unique.name()
        )

        # add and commit individually to get IDs back
        session.add(movie)
        session.commit()

        movies.append(movie)

    roles = []
    for movie in movies:
        for i in range(random.randint(1,5)):

            role = Role(
                character_name=fake.unique.name(),
                actor=fake.unique.name(),
                movie_id=movie.id,
            )

            roles.append(role)

    session.bulk_save_objects(roles)
    session.commit()
    session.close()
