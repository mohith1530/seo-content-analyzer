from flask import Flask, render_template, request
from analyzer.seo_analyzer import analyze_seo

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    url = request.form.get("url")
    keyword = request.form.get("keyword")

    result = analyze_seo(url, keyword)

    return render_template("result.html", result=result)


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)