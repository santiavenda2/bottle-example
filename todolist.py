import sqlite3
from bottle import Bottle, run, request , template

con = sqlite3.connect('todo.db') 

app = Bottle()

@app.route('/todo')
def todo_list():
	c = con.cursor()
	c.execute("SELECT id, task FROM todo WHERE status LIKE '1'")
	result = c.fetchall()
	c.close()
	output = template('make_table', rows=result)
	return output

@app.get('/tasks')
def task_list():
	c = con.cursor()
	c.execute("SELECT id, task, status FROM todo")
	tasks = c.fetchall()
	c.close()
	result = {'tasks': [get_task_dict(t) for t in tasks]}
	return result

@app.get('/tasks/<id>')
def get_task(id):
	c = con.cursor()
	c.execute("SELECT id, task, status FROM todo WHERE id == %s" %id)
	tasks = c.fetchall()
	c.close()
	if len(tasks) > 0:
		t = tasks[0]
		task = get_task_dict(t)
	else:
		task = None
	return task

@app.post('/tasks')
def create_task():
	print request.json
	print "creating task"
	c = con.cursor()
	# TODO revisar sintaxis
	c.execute("INSERT (%s, %s, %s) INTO todo")
	c.close()

@app.delete('/tasks/<id>')
def remove_task(id):
	c = con.cursor()
	# TODO revisar sintaxis
	c.execute("DELETE FROM todo where id == %s" id)
	c.close()


@app.push('tasks/<id>')
def modify_task(id)
	description = request.json['description']
	status = request.json['status']
	# TODO revisar sintaxis
	c = con.cursor()
	c.execute("UPDATE () FROM todo WHERE id == %s")
	c.close()



def get_task_dict(task_as_list):
	return {'id': task_as_list[0], 
			'description': task_as_list[1], 
			'status': task_as_list[2]}

if __name__ == '__main__':
    run(app, host='localhost', port=8080, debug=True, reloader=True)