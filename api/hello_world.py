from . import api

@api.route("/hello_world")
def hello():
    return "Hello World!"