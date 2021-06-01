from flask_migrate import Migrate
from flask import Flask
from models.book import db
from routes.routes import app_routes
from flask_cors import CORS

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/books_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)


app.register_blueprint(app_routes)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


if __name__ == "__main__":
    app.run(debug=True)
