import webtest
import unittest
import todolist

app = webtest.TestApp(todolist.app)


class TodoAppTestCase(unittest.TestCase):

    def test_todo_page(self):
        response = app.get('/todo')
        self.assertEquals(response.status_int, 200)

    def test_get_tasks(self):
        response = app.get('/tasks')
        self.assertEquals(response.status_int, 200)
        tasks_json = response.json
        self.assertEquals(len(tasks_json['tasks']), 4)

    def test_get_task(self):
        response = app.get('/tasks/1')
        self.assertEquals(response.status_int, 200)
        task = response.json
        self.assertEquals(task['id'], 1)
        self.assertEquals(task['status'], 1)

    def test_create_task(self):
        params = {'description': "Test task", 'status':0}
        response = app.post_json('/tasks', params=params)
        self.assertEquals(response.status_int, 200)

    def test_update_task(self):
        id = 5
        params = {'description': "Test task", 'status':0}
        response = app.push_json('/tasks/%s' %id, params=params)
        self.assertEquals(response.status_int, 200)

    def test_remove_task(self):
        id = 5
        response = app.delete('/tasks/%s' %id, params=params)
        self.assertEquals(response.status_int, 200)


if __name__ == '__main__':
    unittest.main()