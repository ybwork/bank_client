from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from settings import Settings

app = Flask(__name__)
app.config.from_object(Settings)
db = SQLAlchemy(app)
import models
migrate = Migrate(app, db)


@app.route('/')
def example():
    response = jsonify({'message': 'ok'})
    response.status_code = 200
    return response


if __name__ == '__main__':
    app.run(debug=True)