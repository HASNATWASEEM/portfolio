from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import os

app = Flask(__name__)

# Projects data
projects = [
    {
        "title": "Landing Page",
        "category": "frontend",
        "desc": "Responsive HTML/CSS landing page",
        "img": "/static/images/project1.jpg"
    },
    {
        "title": "Flask Task Manager",
        "category": "backend",
        "desc": "Task manager built with Flask",
        "img": "/static/images/project2.jpg"
    },
    {
        "title": "ML Predictor",
        "category": "ml",
        "desc": "Machine learning model using Pandas & NumPy",
        "img": "/static/images/project3.jpg"
    }
]

@app.route("/", methods=["GET", "POST"])
def index():
    # Abhi ke liye visitor count static rakha hai kyunki Vercel file save nahi karne deta
    visitor_count = 100 

    if request.method == "POST":
        # Form submission abhi sirf console par dikhayega, save nahi karega
        name = request.form.get("name")
        print(f"New Message from {name}")
        return redirect(url_for("index"))

    return render_template("index.html",
                           projects=projects,
                           visitors=visitor_count)

@app.route("/admin")
def admin():
    # Khali list bhej rahe hain kyunki JSON file Vercel par nahi chalegi
    return render_template("admin.html", messages=[])

if __name__ == "__main__":
    app.run(debug=True)
