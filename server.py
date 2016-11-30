from bottle import route, run, template
from bottle import get, post, request

@route ('/')
def index ():
    return template("index.html")

@route ('/route')
def routes ():
    return template("route.html")

@route ('/requests')
def requests ():
    return template("requests.html")

@get ('/login')
def examples ():
    return template("login.html")

@post ('/login')
def do_login():
  userName = request.forms.get('userName')
  password = request.forms.get('password')
  if password == "bottle":
    return "<h2>valid login, " + userName + ".</h2>"
  else:
    return "<h2>invalid login!</h2>"

run (host = "localhost", port = 8080, debug = True)
