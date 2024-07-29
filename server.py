from flask import Flask, render_template, send_from_directory
app = Flask(__name__)

@app.route("/")
def landing_page():
    return render_template("index.html")
@app.route("/shortcuts")
def shortcuts_page():
    return render_template("shortcuts.html")

@app.route("/formulas")
def formulas_page():
    return render_template("formulas.html")

@app.route("/jinja_documentation")
def vs_shortcuts():
    # return render_template("jinja_documentation.html")
    return send_from_directory('templates', "jinja_documentation.html")

@app.route("/jinja_cheatsheet")
def vs_cheatsheet():
    # return render_template("jinja_cheatsheet.html")
    return send_from_directory('templates', "jinja_cheatsheet.html")



if __name__ == '__main__':
    app.run(debug=True)