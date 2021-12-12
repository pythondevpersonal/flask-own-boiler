from app import app
from flask import render_template,url_for
from flask import request
from werkzeug.utils import redirect
from app.models import Todo
from app import db

@app.route('/', methods=['POST','GET'])
def index():
    if request.method== 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')

        except:
            return 'There was a issue'

    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html',tasks=tasks)

@app.route('/delete/<int:id>', methods=['GET'])
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return "error in deletion"

@app.route('/update/<int:id>', methods=['GET','POST'])
def update(id):
    if request.method == 'POST':
        task = Todo.query.get_or_404(id)
        task.content = request.form['content']

        try:
             db.session.commit()
             return redirect('/')
        except:
            return 'There is an error'

    else:
        task_to_view = Todo.query.get_or_404(id)
        return render_template('view.html',task=task_to_view)