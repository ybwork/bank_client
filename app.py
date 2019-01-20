from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from views import views

app = Flask(__name__)
app.config.from_pyfile('settings.py', silent=True)
app.register_blueprint(views)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


if __name__ == '__main__':
    app.run(debug=True)