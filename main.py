from flask import Flask, render_template

app =Flask(__name__)

projects = [
    {"title": "Text-to-Morse-converter", "description": "A text to morse code converter", "link": "https://github.com/Edu4rt3/Text-to-Morse-converter"},
    {"title": "Portifolio-Website", "description": "A website to show my portifolio", "link": "https://github.com/Edu4rt3/Portifolio-Website"}

]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/projects")
def list_projects():
    return render_template("projects.html", projects=projects)

if __name__ == "__main__":
    app.run(debug=True)