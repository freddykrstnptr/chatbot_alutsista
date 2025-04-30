from flask import Flask, render_template, request, redirect, url_for, session
from rules import chatbot_response

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Dummy akun login
users = {
    "admin@pindad.com": "admin123",
    "user@tapin.id": "tapin456"
}

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        if email in users and users[email] == password:
            session["user"] = email
            return redirect(url_for("index"))
        else:
            return render_template("login.html", error="Email atau password salah.")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

@app.route("/", methods=["GET", "POST"])
def index():
    if "user" not in session:
        return redirect(url_for("login"))

    user_message = ""
    bot_response = ""
    if request.method == "POST":
        user_message = request.form["message"]
        bot_response = chatbot_response(user_message.lower())
    return render_template("index.html", user_message=user_message, bot_response=bot_response)

if __name__ == "__main__":
    app.run(debug=True)