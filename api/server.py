import os.path, json

from flask import Flask, render_template, send_file, send_from_directory

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/project_1")
def open_project_1():
    return render_template('project_1.html')


if __name__ == "__main__":
    app.run(debug=True)
