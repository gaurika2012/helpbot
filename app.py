# app.py
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to HelpBot!</h1><p>Type something in the terminal to talk to the bot.</p>"

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.form["message"].lower()

    if user_input == "quit":
        response = "Goodbye!"
    elif "price" in user_input:
        response = "You can find pricing on our website under the 'Pricing' section."
    elif "account" in user_input:
        response = "You can create an account by clicking the 'Sign up' button."
    else:
        response = "I'm sorry, I didn't understand that."

    return {"reply": response}

if __name__ == "__main__":
    app.run(debug=True)
