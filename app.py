from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
import os

app = Flask(__name__)

# --- MONGODB CONNECTION ---
# Yahan apni string dalein aur <db_password> ko apne naye password se replace karein
MONGO_URI = "mongodb+srv://hasnatwaseem10fw_db_user:HASNAT123@cluster0.9vrdboa.mongodb.net/portfolio_db?retryWrites=true&w=majority"

client = MongoClient(MONGO_URI)
db = client['portfolio_db']
messages_col = db['messages']

projects = [
    {"title": "Landing Page", "category": "frontend", "desc": "Responsive HTML/CSS landing page", "img": "/static/images/project1.jpg"},
    {"title": "Flask Task Manager", "category": "backend", "desc": "Task manager built with Flask", "img": "/static/images/project2.jpg"},
    {"title": "ML Predictor", "category": "ml", "desc": "Machine learning model using Pandas & NumPy", "img": "/static/images/project3.jpg"}
]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        if name and email and message:
            # Data Cloud mein save ho raha hai
            messages_col.insert_one({
                "name": name,
                "email": email,
                "message": message
            })
        return redirect(url_for("index"))

    return render_template("index.html", projects=projects, visitors="Live")

@app.route("/admin")
def admin():
    # Saare messages cloud se nikaal kar admin page par bhej rahe hain
    all_messages = list(messages_col.find({}, {'_id': 0}))
    return render_template("admin.html", messages=all_messages)

if __name__ == "__main__":
    app.run(debug=True)
