from flask import Flask, render_template, request, jsonify

from sources.base import SampleSource

app = Flask(__name__)

# The list of marketplaces to search
SOURCES = [SampleSource()]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/search")
def search():
    query = request.args.get("q", "").strip()
    max_price = request.args.get("max_price", type=float)

    # Ask every source for matching deals and combine them
    results = []
    for source in SOURCES:
        results.extend(source.search(query, max_price))

    # Cheapest first, across all sources
    results = sorted(results, key=lambda d: d["price"])

    return jsonify(results)


if __name__ == "__main__":
    app.run(debug=True, port=5001)