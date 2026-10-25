from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    website_url = request.form["website-url"]

    return f"You submitted: {website_url}"


if __name__ == "__main__":
    app.run(debug=True)
