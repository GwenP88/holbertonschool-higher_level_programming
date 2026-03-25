from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def load_products_from_json():
    with open('products.json') as f:
        products = json.load(f)
    return products

def load_products_from_csv():
    products = []
    with open('products.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            product = {
                "id": int(row["id"]),
                "name": row["name"],
                "category": row["category"],
                "price": float(row["price"])
            }
            products.append(product)
    return products

@app.route('/products')
def get_products():
    source = request.args.get('source')
    product_id = request.args.get('id', None)

    error = None
    products = []

    if source not in ('json', 'csv'):
        error = "Wrong source"
    else:
        if source == 'json':
            products = load_products_from_json()
        else:
            products = load_products_from_csv()

        if product_id:
            found = None
            for product in products:
                if str(product.get('id')) == product_id:
                  found = product
                  break
            
            if found:
                products = [found]
            else:
                error = "Product not found"
                products = []

    return render_template('product_display.html', products=products, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)