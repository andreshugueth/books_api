from flask_sqlalchemy import SQLAlchemy
import uuid

db = SQLAlchemy()


class BookModel(db.Model):
    """Book Model"""
    __tablename__ = 'book'

    id = db.Column(db.String(60), primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    author = db.Column(db.String(120), nullable=False)
    read = db.Column(db.Boolean, nullable=True)

    def __init__(self, book_info):
        """Constructor"""
        self.id = str(uuid.uuid4().hex)
        self.title = book_info.get('title')
        self.author = book_info.get('author')
        self.read = book_info.get('read')

    def save(self):
        """Saves new instance"""
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        """Updates a book record"""
        ignore = ['id']
        for key, item in data.items():
            if key not in ignore:
                setattr(self, key, item)
        db.session.commit()

    def delete(self):
        """Deletes a book record"""
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all_books():
        return BookModel.query.all()

    @staticmethod
    def get_one_book(id):
        """Return a book by id"""
        one_book = BookModel.query.get(id)
        if not one_book:
            return None
        return one_book

    def __repr__(self):
        return '<Book {}>'.format(self.id)


""" class BookSchema(Schema):
    id = fields.Str(dump_only=True)
    title = fields.Str(required=True)
    author = fields.Str(required=False)
    read = fields.Bool(required=True) """
