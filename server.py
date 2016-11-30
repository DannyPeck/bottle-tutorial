# components of the bottle library must be imported by name not with *
from bottle import route, run, template
from bottle import get, post, request

# index route
@route ('/')
def index ():
    return template("index.html")

# route explanation
@route ('/route')
def routes ():
    return template("route.html")

# request explanation
@route ('/requests')
def requests ():
    return template("requests.html")

# retrieves login.html
@get ('/login')
def examples ():
    return template("login.html")

# performs login request
@post ('/login')
def do_login():
    # reads values from the input elements named userName and password
    userName = request.forms.get('userName')
    password = request.forms.get('password')

    # verifies credentials
    if password == "bottle":
    return "<h2>valid login, " + userName + ".</h2>"
    else:
    return "<h2>invalid login!</h2>"

# starts the server running on localhost:8080
run (host = "localhost", port = 8080, debug = True)
