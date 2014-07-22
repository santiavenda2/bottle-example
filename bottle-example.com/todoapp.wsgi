#!/usr/bin/env python
import os
import sys

# Configuro el virtualenv donde quiero trabajar
# activate_this_file = '/home/arsat/.virtualenvs/simulator/bin/activate_this.py'
# execfile(activate_this_file, dict(__file__=activate_this_file))

# Change working directory so relative paths (and template lookup) work again
APP_PATH = os.path.abspath(os.path.dirname(__file__))
os.chdir(APP_PATH)

# Agrego el codigo de la aplicacion al pythonpath
# sys.path.append(APP_PATH)
# print sys.path

# Import app
from todoapp.todolist import app
application = app