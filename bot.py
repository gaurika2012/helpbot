from flask import Flask, request, render_template_string

app = Flask(__name__)

# Your bot logic
def chatbot_response(user_input):
    user_input = user_input.lower()
    if "price" in user_input:
        return "You can find pricing on our website under the 'Pricing' 
section."
    elif "account" in user_input:
        return "You can create an account by clicking the 'Sign up' 
button."
    elif "quit" in user_input:
        return "Goodbye!"
    else:
        return "I'm sorry, I didn't understand that."

# HTML page with a form
HTML = '''
<!DOCTYPE html>
<html>
<head>
    <title>HelpBot</title>
</head>
<body>
    <h1>HelpBot 🤖</h1>
    <form method="POST">
        You: <input name="message" autofocus>
        <input type="submit" value="Send">
    </form>
    {% if response %}
    <p><strong>Bot:</strong> {{ response }}</p>
    {% endif %}
</body>
</html>
'''

@app.route("/", methods=["GET", "POST"])
def home():
    response = ""
    if request.method == "POST":
        message = request.form["message"]
        response = chatbot_response(message)
    return render_template_string(HTML, response=response)

if __name__ == "__main__":
    app.run(debug=True)
