from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_flask():
    return "Olympics Silver Medal"


@app.route("/weightlifting")
def get_winner():
    return "Mirabhai Chanu"


if __name__ == "__main__":
    app.run(port=8080)
