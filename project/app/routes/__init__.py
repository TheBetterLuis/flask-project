from .book_routes import book

def register_routes(app):
    app.register_blueprint(book)

