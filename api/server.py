import os.path, json

from flask import Flask, render_template, send_file, send_from_directory

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/project-1")
def open_projektowanie_wstepne_architektoniczno_urbanistyczne_ii():
    return send_file(path_or_file='./static/files/Projektowanie-wstepne-architektoniczno-urbanistyczne-II-compressed.pdf', as_attachment=False)


@app.route('/test')
def test():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/files/'
    return send_from_directory(filepath, 'test.pdf', as_attachment=False)
    # return send_file(path_or_file="./static/files/test.pdf", as_attachment=False)


if __name__ == "__main__":
    app.run(debug=True)
