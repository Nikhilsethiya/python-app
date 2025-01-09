from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World! Welcome to your Flask app running on localhost."

if __name__ == "__main__":
    app.run(debug=True)
