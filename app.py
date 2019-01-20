from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from settings import Settings
from views import views

app = Flask(__name__)
app.config.from_object(Settings)
app.register_blueprint(views)
db = SQLAlchemy(app)
import models
migrate = Migrate(app, db)


if __name__ == '__main__':
    app.run(debug=True)