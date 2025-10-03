from flask import Flask, render_template, request
from chatbot_logic import get_response

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot_response():
    user_input = request.form["message"]
    response = get_response(user_input)
    return response

if __name__ == "__main__":
    app.run(debug=True)
