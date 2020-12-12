# https://www.atmarkit.co.jp/ait/articles/1808/21/news036_2.html
from flask_cors import CORS
from flask_restless import APIManager
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/todoitems.db"
db = SQLAlchemy(app)
manager = APIManager(app, flask_sqlalchemy_db=db)
# 異なるドメインからのXHRリクエストを処理できるようにする
# 下記だと全ドメインからの全ルートのリクエスト許可＝危険
CORS(app)


class ToDoItem(db.Model):
    __tablename__ = "todoitems"
    item_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    done = db.Column(db.Boolean, nullable=False, default=False)


manager.create_api(ToDoItem, methods=["GET", "POST", "DELETE", "OPTIONS"])
