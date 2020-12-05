from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/todoitems.db'
    db.init_app(app)


class ToDoItem(db.Model):
    __tablename__ = 'todoitems'
    item_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    done = db.Column(db.Boolean, nullable=False, default=False)


class ToDoList:
    def add(self, title):
        """
        todoitemsデータベースにToDoItemを追加する
        """
        item = ToDoItem(title=title)
        db.session.add(item)
        db.session.commit()

    def delete(self, item_id):
        """
        todoitemsデータベースから指定されたIDのToDoItemを削除する
        """
        item = ToDoItem.query.filter_by(item_id=item_id).first()
        db.session.delete(item)
        db.session.commit()

    def get_all(self):
        """
        ToDo項目を含むリストを返送する
        """
        items = ToDoItem.query.all()
        return items

    def delete_doneitem(self):
        """
        doneメンバの値がTrueとなっている項目（完了した項目）をリストから削除する
        """
        ToDoItem.query.filter_by(done=True).delete()
        db.session.commit()

    def update_done(self, items):
        """
        指定されたIDのdoneメンバの値を反転する
        """
        for item in self.get_all():
            if item.item_id in items:
                item.done = True
            else:
                item.done = False
        db.session.commit()
