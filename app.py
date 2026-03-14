from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

projects = [
    {"title": "Landing Page", "category": "frontend", "desc": "Responsive HTML/CSS landing page", "img": "/static/images/project1.jpg"},
    {"title": "Flask Task Manager", "category": "backend", "desc": "Task manager built with Flask", "img": "/static/images/project2.jpg"},
    {"title": "ML Predictor", "category": "ml", "desc": "Machine learning model using Pandas & NumPy", "img": "/static/images/project3.jpg"}
]

@app.route("/", methods=["GET", "POST"])
def index():
    # File writing khatam kar di hai taake crash na ho
    visitor_count = "Live" 
    
    if request.method == "POST":
        return redirect(url_for("index"))

    return render_template("index.html", projects=projects, visitors=visitor_count)

@app.route("/admin")
def admin():
    return render_template("admin.html", messages=[])

if __name__ == "__main__":
    app.run(debug=True)
