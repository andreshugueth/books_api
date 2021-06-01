from flask import request
from models import book


def get_books():
    """Returns list of books"""
    result = book.BookModel.query.all()
    new_list = []
    for item in result:
        new_list.append({
            "id": item.id,
            "title": item.title,
            "author": item.author,
            "read": item.read
        })
    return new_list


def get_book_by_id(id):
    """Returns an specific book"""
    result = book.BookModel.get_one_book(id)
    if not result:
        return {"msg": "Book not found"}
    return {
        "id": result.id,
        "title": result.title,
        "author": result.author,
        "read": result.read
    }


def create_book(data):
    """Creates a book record"""
    instance = book.BookModel(data)
    instance.save()
    return {"msg": f'Book: {instance.id} has been created successfully'}


def updating_book(data):
    """Update a book record"""
    result = book.BookModel.get_one_book(data["id"])
    if not result:
        return {"msg": f'Book {data["id"]} not found'}

    result.update(data)
    return {"msg": f'Book: {data["id"]} has been updated successfully'}


def deleting_book(id):
    """Deletes a book"""
    result = book.BookModel.get_one_book(id)
    if not result:
        return {"msg": f'Book: {id} not found'}

    result.delete()
    return {"msg": f'Book: {id} has been deleted successfully'}
