
from bottle import Bottle, run, request, template, response, HTTPError, HTTP_CODES

from dao import ToDoSqlDAO

dao = ToDoSqlDAO('todo.db')

app = Bottle()


@app.route('/todo')
def todo_list():
    tasks = dao.find_tasks()
    output = template('make_table', rows=tasks)
    return output


@app.get('/tasks')
def task_list():
    tasks = dao.find_tasks()
    result = {'tasks': [get_task_dict(t) for t in tasks]}
    return result


@app.get('/tasks/<task_id>')
def get_task(task_id):
    task = dao.find_task_by_id(task_id)
    if task:
        return get_task_dict(task)
    else:
        return HTTPError(404, HTTP_CODES[404])


@app.post('/tasks')
def create_task():
    params = request.json
    description = params['description']
    dao.create_task(description)
    response.status = 201
    return {'id': 0}


@app.delete('/tasks/<task_id>')
def remove_task(task_id):
    dao.delete_task(task_id)


@app.put('/tasks/<task_id>')
def modify_task(task_id):
    description = request.json['description']
    status = request.json['status']
    dao.modify_task(task_id, description, status)


def get_task_dict(task_as_list):
    return {'id': task_as_list[0], 
            'description': task_as_list[1], 
            'status': task_as_list[2]}

if __name__ == '__main__':
    run(app, host='localhost', port=8080, debug=True, reloader=True)