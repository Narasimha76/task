from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime, timedelta

app = Flask(__name__)

# Sample in-memory database
tasks = []

@app.route('/')
def index():
    now = datetime.now()
    return render_template('index.html', tasks=[], now=now)

@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    due_date_str = request.form.get('due_date')

    if task and due_date_str:
        due_date = datetime.strptime(due_date_str, '%Y-%m-%d')
        tasks.append({'task': task, 'due_date': due_date})

    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete(task_id):
    if 0 <= task_id < len(tasks):
        del tasks[task_id]
    if not tasks:
        return redirect(url_for('index'))
    return redirect(url_for('view_tasks'))

@app.route('/view_tasks')
def view_tasks():
    now = datetime.now()
    return render_template('view_tasks.html', tasks=tasks, now=now)

if __name__ == '__main__':
    app.run(debug=True)
