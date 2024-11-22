from .book_routes import book
from .author_routes import author
from .genre_routes import genre 
from .editorial_routes import editorial

def register_routes(app):
    app.register_blueprint(book)
    app.register_blueprint(author)
    app.register_blueprint(genre)
    app.register_blueprint(editorial)


