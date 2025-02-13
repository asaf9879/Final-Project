import os

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


# Database configuration
db_address = '127.0.0.1'
db_name = 'tasksdb'
db_user = 'asaf'
db_pass = '1234'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{db_user}:{db_pass}@{db_address}/{db_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Model for Task
class Tasks(db.Model):
    task_id = db.Column(db.Integer, primary_key=True)  # Task ID column
    task = db.Column(db.String(255), nullable=False)  # Task description
    completed = db.Column(db.Boolean, nullable=False, default=False)  # Task completion status
    date_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)  # Date added
    user_name = db.Column(db.String(255), nullable=True)  # Username for the task creator
    priority = db.Column(db.String(50), nullable=False)  # Task priority
    deadline = db.Column(db.DateTime, nullable=True)  # Task deadline

# Route for displaying tasks on the main page
@app.route('/')
def index():
    tasks = Tasks.query.all()  # Get all tasks from the database
    return render_template('index.html', tasks=tasks)

# Route for adding a new task
@app.route('/add_task', methods=['POST'])
def add_task():
    task_name = request.form['task']  # Get task name from the form field 'task'
    priority = request.form['priority']
    deadline = request.form.get('deadline', '')

    if deadline:
        deadline = datetime.strptime(deadline, "%Y-%m-%d")
    else:
        deadline = None

    new_task = Tasks(
        task=task_name,
        priority=priority,
        deadline=deadline,
        completed=False,
    )
    db.session.add(new_task)
    db.session.commit()

    return redirect(url_for('index'))

# Route for marking a task as done
@app.route('/mark_done/<int:task_id>', methods=['POST'])
def mark_done(task_id):
    task = Tasks.query.get_or_404(task_id)
    task.completed = True
    db.session.commit()

    return redirect(url_for('index'))  # Redirect back to the index page after marking done

@app.route('/delete_task/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    task = Tasks.query.get_or_404(task_id)  # Find the task by its ID
    db.session.delete(task)  # Delete the task
    db.session.commit()  # Commit the transaction to the database

    return redirect(url_for('index'))  # Redirect back to the index page after deletion

if __name__ == '__main__':
    app.run(debug=True)
