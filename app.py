from flask import Flask, render_template, request, jsonify

from sources.dummyjson import DummyJsonSource

app = Flask(__name__)

# Active marketplaces. Add EbaySource() here later when keys are ready.
SOURCES = [DummyJsonSource()]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/search")
def search():
    query = request.args.get("q", "").strip()
    max_price = request.args.get("max_price", type=float)

    results = []
    for source in SOURCES:
        try:
            results.extend(source.search(query, max_price))
        except Exception as err:
            # One source failing shouldn't break the whole search.
            print("Source", source.name, "failed:", err)

    results = sorted(results, key=lambda d: d["price"])
    return jsonify(results)


if __name__ == "__main__":
    app.run(debug=True, port=5001)