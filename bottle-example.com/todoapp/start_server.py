from bottle import run

from todolist import app

server = ""
print "Running on: %s" % server
if server == "cherrypy":
    run(app, server="cherrypy", host='localhost', port=9190)
elif server == "paste":
    run(app, server="paste", host='localhost', port=9190)
elif server == "gunicorn":
    run(app, server="gunicorn", host='localhost', port=9190)
elif server == "apache":
    #TODO
    pass
else:
    run(app, host='localhost', port=9190, debug=True, reloader=True)