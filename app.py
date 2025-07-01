from flask import Flask, render_template, request
import json

app = Flask(__name__)

with open("data/progress_data.json") as f:
    DATA = json.load(f)

@app.route("/", methods=["GET", "POST"])
def index():
    checked = request.form.getlist("checked")
    return render_template("index.html", data=DATA, checked=checked)

if __name__ == "__main__":
    app.run(debug=True)
