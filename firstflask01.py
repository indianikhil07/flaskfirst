from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"
@app.route("/about")
def about():
    return "I am nikhil singh"
if __name__ == "__main__":
    app.run(debug = True)

app.run()
