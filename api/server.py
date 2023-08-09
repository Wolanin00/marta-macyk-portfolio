import os.path

from flask import Flask, render_template, send_file

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/project-1")
def open_projektowanie_wstepne_architektoniczno_urbanistyczne_ii():
    return send_file(path_or_file='./static/files/Projektowanie-wstepne-architektoniczno-urbanistyczne-II-compressed.pdf', as_attachment=False)


@app.route('/test')
def test():
    return send_file(path_or_file=os.path.join(os.path.dirname(__file__), "static/files/test.pdf"), as_attachment=False)


if __name__ == "__main__":
    app.run(debug=True)
