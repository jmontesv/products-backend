from flask import Flask, jsonify, request
from flask_cors import CORS
from products import filter_by_name, filter_by_price_min, filter_by_price_max, filter_by_page
from utils import load_json

app = Flask(__name__)
CORS(app)

@app.route("/")
def main():
    return "Bienvenido!"

@app.route("/products")
def products():
    products = load_json("products.json")
    name = request.args.get("name")
    price_min = request.args.get("price_min")
    price_max = request.args.get("price_max")
    page = request.args.get("page")
    per_page = request.args.get("per_page")
    if name:
        products_filtered = filter_by_name(name, products)
        products = products_filtered
    if price_min:
        products_filtered = filter_by_price_min(int(price_min), products)
        products = products_filtered
    if price_max:
        products_filtered = filter_by_price_max(int(price_max), products)
        products = products_filtered
    if page and per_page:
        products_filtered = filter_by_page(int(page), int(per_page), products)
        products = products_filtered
    return jsonify(products)

# Punto de entrada del servidor Flask
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)