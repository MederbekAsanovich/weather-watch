from flask import Flask
from flask_migrate import Migrate
from models import db
from routes import api
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(api, url_prefix='/api/v1')

if __name__ == '__main__':
    app.run(debug=True)
