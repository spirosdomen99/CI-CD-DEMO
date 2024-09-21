from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__, template_folder=os.path.abspath('templates'))  # Use absolute path for templates folder

# In-memory list to store to-do items
todos = []

@app.route('/')
def home():
    # Print the contents of the 'templates' directory for debugging
    print("Templates directory contents:", os.listdir(os.path.abspath('templates')))
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
    # Get the task from the form
    task = request.form.get('task')
    if task:
        todos.append(task)
    return redirect(url_for('home'))

@app.route('/delete/<int:task_id>')
def delete(task_id):
    # Delete the task by index (task_id)
    if 0 <= task_id < len(todos):
        todos.pop(task_id)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
