from __init__ import app

if __name__ == "__main__":
    app.run(debug=True, threaded=True)

@app.route("/")
def root():
    return app.send_static_file('stats/stats.html')