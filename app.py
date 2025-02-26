from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "This is a simple python flask app, and it is Docker container project by Nelson."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
