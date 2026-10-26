import base64
from io import BytesIO

import qrcode
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    website_url = request.form["website-url"]

    qr_image = qrcode.make(website_url)

    image_data = BytesIO()
    qr_image.save(image_data, format="PNG")

    encoded_image = base64.b64encode(image_data.getvalue()).decode("utf-8")

    return render_template(
        "result.html", qr_code=encoded_image, website_url=website_url
    )


if __name__ == "__main__":
    app.run(debug=True)
