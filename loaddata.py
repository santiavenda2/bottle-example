import sqlite3


def load_data(db_name):
    con = sqlite3.connect(db_name) # Warning: This file is created in the current directory
    con.execute("DROP TABLE todo")
    con.execute("CREATE TABLE todo (id INTEGER PRIMARY KEY, task char(100) NOT NULL, status bool NOT NULL)")
    con.execute("INSERT INTO todo (task,status) VALUES ('Visit the Python website',1)")
    con.execute("INSERT INTO todo (task,status) VALUES ('Visit the Bottle website',1)")
    con.execute("INSERT INTO todo (task,status) VALUES ('Test various editors for and check the syntax highlighting',0)")
    con.execute("INSERT INTO todo (task,status) VALUES ('Choose your favorite WSGI-Framework',0)")
    con.commit()

if __name__ == "__main__":
    load_data('todo.db')