# https://www.atmarkit.co.jp/ait/articles/1807/31/news042.html
from flask import Flask, render_template, redirect, request
from todo import ToDoList, init_db

app = Flask(__name__)

db = init_db(app)

todolist = ToDoList()
myname = 'shun'


@app.route('/')
def show_todoliist():
    return render_template('showtodo.html', todolist=todolist.get_all())


@app.route('/additem', methods=['POST'])
def add_item():
    title = request.form['title']
    if not title:
        return redirect('/')
    todolist.add(title)
    return redirect('/')


@app.route('/deleteitem/<int:item_id>')
def delete_todoitem(item_id):
    todolist.delete(item_id)
    return redirect('/')


@app.route('/updatedone', methods=['POST'])
def update_done(item_id):
    keys = request.form.keys()
    items = [int(x) for x in keys]
    todolist.update_done(items)
    return redirect('/')


@app.route('/deletealldoneitems')
def delete_alldoneitems():
    todolist.delete_doneitem()
    return redirect('/')


@app.route('/hello', methods=['GET'])
def hello_test():
    return render_template('hello.html', myname=myname, say=request.args.get('say'), to=request.args.get('to'))
