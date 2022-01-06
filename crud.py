from model import db, User, Movie, Rating, connect_to_db


def get_users():
    """Get all users"""
    
    return User.query.all()

def create_user(email, password):
    """Create and return new user"""
    user = User(email=email, password=password)
    
    db.session.add(user)
    db.session.commit()

    return user

def create_movie(title, overview, release_date, poster_path):
    """Create and return new movie"""
    movie = Movie(
        title=title, 
        overview=overview, 
        release_date= release_date,
        poster_path=poster_path
    )
    
    db.session.add(movie)
    db.session.commit()

    return movie

def get_movies():
    """Return a list with all movies"""

    return Movie.query.all()

def get_movie_by_id(movie_id):
    """"Return the movie details by movie_id"""
    return Movie.query.get(movie_id)

def create_rating(user, movie, score):

    """Create and return a new rating."""

    rating = Rating(user=user, movie=movie, score=score)

    db.session.add(rating)
    db.session.commit()

    return rating
    
if __name__ == "__main__":
    # DebugToolbarExtension(app)
    from server import app
    connect_to_db(app)
