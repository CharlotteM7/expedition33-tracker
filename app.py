from flask import Flask, render_template, request
import json
import os

app = Flask(__name__)

with open("data/progress_data.json") as f:
    DATA = json.load(f)

@app.route("/", methods=["GET", "POST"])
def index():
    checked = request.form.getlist("checked")
    return render_template("index.html", data=DATA, checked=checked)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
