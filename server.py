"""Step 9: the private village on your own computer.
Run:  py server.py   then open http://localhost:5007/village/"""
from flask import Flask, send_from_directory
import village_data          # the Step 3 script

app = Flask(__name__)


@app.route("/village/")
def village():
    return send_from_directory("village", "index.html")


@app.route("/village/village_data.json")
def data():
    village_data.main()      # rebuild from the latest logs every time the page asks
    return send_from_directory("village", "village_data.json")


if __name__ == "__main__":
    app.run(port=5007)
