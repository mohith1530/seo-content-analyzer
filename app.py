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
    app.run(debug=True)