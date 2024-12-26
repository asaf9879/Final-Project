from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    task_name = request.form['task_name']
    priority = request.form['priority']
    deadline = request.form.get('deadline', '')
    tasks.append({'name': task_name, 'done': False, 'priority': priority, 'deadline': deadline})
    return redirect(url_for('index'))

@app.route('/mark_done/<int:task_index>', methods=['POST'])
def mark_done(task_index):
    tasks[task_index]['done'] = True
    return redirect(url_for('index'))

@app.route('/delete_task/<int:task_index>', methods=['POST'])
def delete_task(task_index):
    tasks.pop(task_index)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()