class ToDoItem:
    item_id = 0

    def __init__(self, title):
        self.title = title
        self.done = False
        self.item_id = ToDoItem.item_id
        ToDoItem.item_id += 1


class ToDoList:
    def __init__(self):
        self.todolist = []

    def add(self, title):
        """
        self.todoListにToDo項目を追加する
        """
        item = ToDoItem(title)
        self.todolist.append(item)

    def delete(self, item_id):
        """
        指定されたIDのToDo項目を削除する
        """
        self.todolist = [x for x in self.todolist if x.item_id != item_id]

    def update(self, item_id):
        """
        指定されたIDのdoneメンバの値を反転する
        """
        item = [x for x in self.todolist if x.item_id == item_id]
        item[0].done = not item[0].done

    def get_all(self,):
        """
        ToDo項目を含むリストを返送する
        """
        return self.todolist

    def delete_doneitem(self):
        """
        doneメンバの値がTrueとなっている項目（完了した項目）をリストから削除する
        """
        self.todolist = [x for x in self.todolist if not x.done]
