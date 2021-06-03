from flask_migrate import Migrate
from flask import Flask, make_response, jsonify
from models.book import db
from routes.routes import app_routes
from flask_cors import CORS
from flasgger import Swagger

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/books_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)


app.register_blueprint(app_routes)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.errorhandler(404)
def not_found(error):
    """ 404 Error
    ---
    responses:
      404:
        description: a resource was not found
    """
    return make_response(jsonify({'error': "Not found"}), 404)


app.config['SWAGGER'] = {
    'title': 'Books Restful API',
    'uiversion': 3
}

Swagger(app)

if __name__ == "__main__":
    app.run(debug=True)
