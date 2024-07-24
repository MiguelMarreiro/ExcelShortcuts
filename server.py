from flask import Flask, render_template
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

if __name__ == '__main__':
    app.run(debug=True)