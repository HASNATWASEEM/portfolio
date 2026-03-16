from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
import os

app = Flask(__name__)

# --- MONGODB CONNECTION ---
# Replace <db_password> with your actual password if needed
MONGO_URI = "mongodb+srv://hasnatwaseem10fw_db_user:HASNAT123@cluster0.9vrdboa.mongodb.net/portfolio_db?retryWrites=true&w=majority"

client = MongoClient(MONGO_URI)
db = client['portfolio_db']
messages_col = db['messages']

# --- PROJECTS LIST (multi-image support) ---
projects = [
    {
        "title": "DIABETES PREDICTION SYSTEM",
        "category": "Frontend",
        "desc": "Machine learning model using Pandas & NumPy",
        "images": [
            "/static/images/project1-1.jpg",
            "/static/images/project1-2.jpg",
            "/static/images/project1-3.jpg"
        ]
    },
    {
        "title": "DUBBING TOOL",
        "category": "Backend",
        "desc": "DUBBING TOOL built with Flask",
        "images": [
            "/static/images/project2-1.jpg",
            "/static/images/project2-2.jpg"
        ]
    },
    {
        "title": "PORTFOLIO PROJECT",
        "category": "ML",
        "desc": "PORTFOLIO WITH HTML/CSS",
        "images": [
            "/static/images/project3-1.jpg"
        ]
    }
]

# --- ROUTES ---

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        if name and email and message:
            # Save message to MongoDB
            messages_col.insert_one({
                "name": name,
                "email": email,
                "message": message
            })
        return redirect(url_for("index"))

    return render_template("index.html", projects=projects, visitors="Live")

@app.route("/admin")
def admin():
    # Fetch all messages from MongoDB for admin view
    all_messages = list(messages_col.find({}, {'_id': 0}))
    return render_template("admin.html", messages=all_messages)

# --- RUN SERVER ---
if __name__ == "__main__":
    app.run(debug=True)
