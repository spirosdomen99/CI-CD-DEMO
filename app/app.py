from flask import Flask,render_template, request, redirect, url_for
import os

app = Flask(__name__)

todo = []

@app.route('/')
def home():
 print("Templates dir contents:", os.listdir('templates'))
 return render_template('index.html',todo=todo)

@app.route('/add',methods=['POST'])
def add():
 task = request.form.get('task')
 if task:
  todo.append(task)
 return redirect(url_for('home'))

@app.route('/delete/<int:task_id>')
def delete(task_id):
 if 0<= task_id < len(todo):
  todo.pop(task_id)
 return	redirect(url_for('home'))

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug =True)