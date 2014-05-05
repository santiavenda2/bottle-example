__author__ = 'santiago'


from abc import ABCMeta, abstractmethod
import sqlite3


class ToDoDAO(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def find_tasks(self):
        pass

    @abstractmethod
    def find_task_by_id(self, task_id):
        pass

    @abstractmethod
    def create_task(self, description):
        pass

    @abstractmethod
    def modify_task(self, task_id, description, status):
        pass

    @abstractmethod
    def delete_task(self, task_id):
        pass



class ToDoMongoDAO():

    pass


class ToDoSqlDAO(ToDoDAO):

    def __init__(self, db_name):
        # Warning: This file is created in the current directory
        self.con = sqlite3.connect(db_name)

    def find_tasks(self):
        c = self.con.cursor()
        c.execute("SELECT id, task, status FROM todo")
        results = c.fetchall()
        return results

    def find_task_by_id(self, task_id):
        c = self.con.cursor()
        c.execute("SELECT id, task, status FROM todo WHERE id=?", task_id)
        result = c.fetchone()
        c.close()
        return result

    def create_task(self, description):
        try:
            with self.con:
                stm = "INSERT INTO todo (task,status) VALUES (\'%s\',0)" % (description,)
                self.con.execute(stm)
        except Exception as e:
            print e.message
            raise e

    def modify_task(self, task_id, description, status):
        with self.con:
            self.con.execute("UPDATE todo SET task=\'%s\' , status=\'%s\' WHERE id == \'%s'" % (description, status, task_id))

    def delete_task(self, task_id):
        with self.con:
            self.con.execute("DELETE FROM todo where id == ?", task_id)

    def clean_todo_table(self):
        with self.con:
            self.con.execute("DROP TABLE todo")
            self.con.execute("CREATE TABLE todo (id INTEGER PRIMARY KEY, task char(100) NOT NULL, status bool NOT NULL)")

    def load_data(self):
        self.clean_todo_table()
        with self.con:
            self.create_task('Visit the Python website')
            self.create_task('Visit the Bottle website')
            self.create_task('Test various editors for and check the syntax highlighting')
            self.create_task('Choose your favorite WSGI-Framework')


