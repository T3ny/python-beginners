from flask import Flask, render_template, request
from bot import Bot

app = Flask(__name__)

chatbot = Bot(name="Chattie", age=3, sex="Non-binary")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.form.get("user_input")
    response = chatbot.questions(user_input)
    return render_template("index.html", user_input=user_input, response=response)

if __name__ == "__main__":
    app.run(debug=True)
