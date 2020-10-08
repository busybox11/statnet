from __init__ import app # pylint: disable=no-name-in-module

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(debug=True)