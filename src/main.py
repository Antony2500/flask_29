from flask import Flask

app = Flask(__name__)

@app.route("/documentation")
def documentation():
    return True


if __name__ == "__main__":
    app.run(debug=True)