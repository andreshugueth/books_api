
from flask import request
from models import book
import json

books_list = [
    {
        "id": 1,
        "title": "On the Road",
        "author": "Jack Kerouac",
        "read": "True"
    },
]


def get_books():
    """Returns list of books"""
    result = book.BookModel.query.all()
    print(json.dumps([element.as_dict() for element in result]))
    return [element.as_dict() for element in result]


def get_book_by_id(id):
    """Returns an specific book"""
    result = book.BookModel.get_one_book(id)
    if not result:
        return {"msg": "Book not found"}
    return result


def create_book(data):
    """Creates a book record"""
    print(data)
    instance = book.BookModel(data)
    instance.save()
    return {"msg": f'Book: {instance.id} has been created successfully'}


def updating_book(data):
    for i in range(len(books_list)):
        if books_list[i]["id"] == data["id"]:
            books_list[i] = data
            return {"msg": f'Book: {data["id"]} has been updated successfully'}
    return {"msg": f'Book: {data["id"]} not found'}


def deleting_book(id):
    for i in range(len(books_list)):
        if books_list[i]["id"] == id:
            books_list.pop(i)
            return {"msg": f'Book: {id} has been deleted successfully'}
    return {"msg": f'Book: {id} not found'}
