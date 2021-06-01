
from flask import Blueprint, request, make_response, abort
from flask import jsonify

from controller.controller import get_books, get_book_by_id, create_book, updating_book, deleting_book

app_routes = Blueprint('app_routes', __name__, url_prefix='/api')


@app_routes.route('/books', methods=["GET"], strict_slashes=False)
def list_books():
    return jsonify(get_books())


@app_routes.route('/book/<id>', methods=['GET'], strict_slashes=False)
def book(id):
    return jsonify(get_book_by_id(id))


@app_routes.route('/book', methods=["POST"], strict_slashes=False)
def add_books():
    """Creates a book record"""
    if not request.get_json():
        abort(400, description="Not a JSON")
    data = request.get_json()
    return jsonify(create_book(data))


@app_routes.route('/book', methods=["PUT"])
def update_book():
    data = request.get_json()
    return jsonify(updating_book(data))


@app_routes.route('/book/<int:id>', methods=["DELETE"])
def delete_book(id):
    return jsonify(deleting_book(id))
