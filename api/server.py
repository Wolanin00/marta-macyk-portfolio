import os.path, json

from flask import Flask, render_template, send_file, send_from_directory

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/project-1")
def open_projektowanie_wstepne_architektoniczno_urbanistyczne_ii():
    url = 'https://github.com/Wolanin00/marta-macyk-portfolio/blob/main/api/static/files/Projektowanie-wstepne-architektoniczno-urbanistyczne-II-compressed.pdf'
    filename = wget.download(url)
    return render_template('index.html')


@app.route('/test')
def test():
    workingdir = os.path.abspath(os.getcwd())
    # test
    filepath = workingdir + '/static/files/'
    return send_from_directory(filepath, 'test.pdf', as_attachment=False)
    # return send_file(path_or_file="./static/files/test.pdf", as_attachment=False)


if __name__ == "__main__":
    app.run(debug=True)
