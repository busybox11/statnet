from __init__ import app
import os
app._static_folder = os.path.abspath("static/")

from flask import Flask, request, send_from_directory

if __name__ == "__main__":
    app.run(debug=True, threaded=True)

@app.route("/")
def root():
    root_dir = os.path.dirname(os.getcwd())
    return send_from_directory(os.path.join(root_dir, 'static'), 'stats.html')