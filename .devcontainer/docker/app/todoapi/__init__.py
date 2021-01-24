import os

from flask import Flask
from flask_cors import CORS
from flask_restless import APIManager
from flask_sqlalchemy import SQLAlchemy

from todoapi.config import Config, DevConfig, DockerConfig

config = {
    "default": Config,
    "dev": DevConfig,
    "docker": DockerConfig
}

app = Flask(__name__, instance_relative_config=True)

cfg = config[os.getenv("TODOAPI_ENV", default="default")]
app.config.from_object(cfg)
app.config.from_pyfile("config.cfg")

db = SQLAlchemy(app)
manager = APIManager(app, flask_sqlalchemy_db=db)
CORS(app)


class ToDoItem(db.Model):
    __tablename__ = "todoitems"
    item_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    done = db.Column(db.Boolean, nullable=False, default=False)


manager.create_api(ToDoItem,
                   methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
                   results_per_page=100
                   )


@app.route("/")
def index():
    return f'{app.config["TODOAPI_CONFIG"]},<br>{app.config["TODOAPI_CONFIG2"]}'
