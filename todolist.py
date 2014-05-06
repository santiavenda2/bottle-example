
from bottle import Bottle, run, request, template, response, HTTPError, HTTP_CODES

from dao import ToDoSqlDAO

dao = ToDoSqlDAO('todo.db')

app = Bottle()

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
    task_id = dao.create_task(description)
    response.status = 201
    return {'task_id': task_id}


@app.delete('/tasks/<task_id>')
def remove_task(task_id):
    dao.delete_task(task_id)
    response.status = 204


@app.put('/tasks/<task_id>')
def modify_task(task_id):
    description = request.json['description'] if 'description' in request.json else None
    status = request.json['status'] if 'status' in request.json else None
    dao.modify_task(task_id, description, status)
    response.status = 204


def get_task_dict(task_as_list):
    return {'id': task_as_list[0], 
            'description': task_as_list[1], 
            'status': task_as_list[2]}

if __name__ == '__main__':
    server = "gunicorn"
    print "Runnning on: %s" % server
    if server == "cherrypy":
        run(app, server="cherrypy", host='localhost', port=9090)
    elif server == "paste":
        run(app, server="paste", host='localhost', port=9090)
    elif server == "gunicorn":
        run(app, server="gunicorn", host='localhost', port=9090)
    elif server == "apache":
        #TODO
        pass
    else:
        run(app, host='localhost', port=9090, debug=True, reloader=True)