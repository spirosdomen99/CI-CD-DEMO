from flask import Flask,render_template, request, redirect,url_for

app = Flask(__name__)

todos = []

@app.route('/')
def home():
 return render_template('index.html',todos=todos)

@app.route('/add',methods=['POST'])
def add():
 task = request.form.get('task')
 if task:
  todos.append(task)
 return redirect(url_for('home'))

@app.route('/delete/<int:task_id>')
def delete(task_id):
 if 0<= task_id < len(todos):
  todos.pop(task_id)
 return	redirect(url_for('home'))

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug =True)