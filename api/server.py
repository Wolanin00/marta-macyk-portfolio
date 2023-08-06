from flask import Flask, render_template, send_file

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route("/Projektowanie-wstepne-architektoniczno-urbanistyczne-II")
def open_projektowanie_wstepne_architektoniczno_urbanistyczne_ii():
    return send_file(path_or_file='static/file/Projektowanie-wstepne-architektoniczno-urbanistyczne-II-compressed.pdf', as_attachment=False)


if __name__ == "__main__":
    app.run(debug=True)
