import webtest
import unittest
import todolist
from mock import patch


app = webtest.TestApp(todolist.app)


class TodoAppTestCase(unittest.TestCase):

    @patch('todolist.dao')
    def test_todo_page(self, mock_dao):
        mock_dao.find_tasks.return_value = [(1, "prueba", 0)]
        response = app.get('/todo')
        self.assertEquals(response.status_int, 200)
        mock_dao.find_tasks.assert_called_once_with()

    @patch('todolist.dao')
    def test_get_tasks(self, mock_dao):
        mock_dao.find_tasks.return_value = [(1, "prueba", 0)]

        response = app.get('/tasks')
        self.assertEquals(response.status_int, 200)
        tasks_json = response.json
        self.assertTrue(len(tasks_json['tasks']) == 1)
        self.assertEqual(tasks_json['tasks'][0], {"id": 1, "description": "prueba", "status": 0})
        mock_dao.find_tasks.assert_called_once_with()

    @patch('todolist.dao')
    def test_get_empty_tasks(self, mock_dao):
        mock_dao.find_tasks.return_value = []

        response = app.get('/tasks')
        self.assertEquals(response.status_int, 200)
        tasks_json = response.json
        self.assertTrue(len(tasks_json['tasks']) == 0)

        mock_dao.find_tasks.assert_called_once_with()

    @patch('todolist.dao')
    def test_get_task(self, mock_dao):
        mock_dao.find_task_by_id.return_value = (1, "prueba", 1)

        response = app.get('/tasks/1')
        task = response.json

        self.assertEquals(response.status_int, 200)
        self.assertEquals(task['id'], 1)
        self.assertEquals(task['status'], 1)
        self.assertEquals(task['description'], "prueba")
        mock_dao.find_task_by_id.assert_called_once_with('1')

    @patch('todolist.dao')
    def test_get_inexistent_task(self, mock_dao):
        mock_dao.find_task_by_id.return_value = None

        response = app.get('/tasks/1', expect_errors=True)

        self.assertEquals(response.status_int, 404)
        mock_dao.find_task_by_id.assert_called_once_with('1')

    @patch('todolist.dao')
    def test_create_task(self, mock_dao):
        mock_dao.create_task.return_value = 1
        params = {'description': "Test task", 'status': 0}
        response = app.post_json('/tasks', params=params)
        self.assertEquals(response.status_int, 201)
        mock_dao.create_task.assert_called_once_with("Test task")

    @patch('todolist.dao')
    def test_update_task(self, mock_dao):
        mock_dao.modify_task.return_value = None

        task_id = 5
        params = {'description': "Test task", 'status': 0}
        response = app.put_json('/tasks/%s' % task_id, params=params)
        self.assertEquals(response.status_int, 200)

        mock_dao.modify_task.assert_called_once_with("5", "Test task", 0)

    @patch('todolist.dao')
    def test_remove_task(self, mock_dao):
        mock_dao.delete_task.return_value = None

        task_id = 5
        response = app.delete('/tasks/%s' % task_id)
        self.assertEquals(response.status_int, 200)

        mock_dao.delete_task.assert_called_once_with("5")


if __name__ == '__main__':
    unittest.main()