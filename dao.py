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
        self.con = sqlite3.connect(db_name)

    def find_tasks(self):
        c = self.con.cursor()
        c.execute("SELECT id, task FROM todo")
        results = c.fetchall()
        return results

    def find_task_by_id(self, task_id):
        c = self.con.cursor()
        c.execute("SELECT id, task FROM todo WHERE id=%s" % id)
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
            self.con.execute("DELETE FROM todo where id == %s" % task_id)



