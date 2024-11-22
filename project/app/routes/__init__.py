from .book_routes import book
from .author_routes import author
from .genre_routes import genre 
from .editorial_routes import editorial
from .review_routes import review
from .user_routes import user

def register_routes(app):
    app.register_blueprint(book)
    app.register_blueprint(author)
    app.register_blueprint(genre)
    app.register_blueprint(editorial)
    app.register_blueprint(review)
    app.register_blueprint(user)


