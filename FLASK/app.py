from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Required for flash messages

posts = [
    {"title": "first article", "content": "this is my first article in this blog"},
    {"title": "second article", "content": "this is my second article in this blog"}
]

@app.route("/")
def home():
    return render_template("home.html", posts=posts)

@app.route("/add/", methods=["GET", "POST"])
def add_post():
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        content = request.form.get("content", "").strip()
        
        # Basic validation
        if not title or not content:
            flash("Both title and content are required!", "error")
            return render_template("add.html")
        
        if len(title) > 100:
            flash("Title must be 100 characters or less!", "error")
            return render_template("add.html")
        
        posts.append({"title": title, "content": content})
        flash(f"Post '{title}' has been successfully added!", "success")
        return redirect(url_for("home"))
    
    return render_template("add.html")

if __name__ == "__main__":
    app.run(debug=True)