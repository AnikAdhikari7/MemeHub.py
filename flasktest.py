from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello from flusk"

app.run(host="0.0.0.0", port="8080")