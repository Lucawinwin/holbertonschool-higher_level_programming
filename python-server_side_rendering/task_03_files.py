import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)

def read_json():
    with open('products.json', 'r') as file:
        return json.load(file)

def read_csv():
    products = []
    with open('products.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['price'] = float(row['price'])  # Convert price to float
            products.append(row)
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    
    if source == 'json':
        products = read_json()
    elif source == 'csv':
        products = read_csv()
    else:
        return render_template('product_display.html', error="Wrong source")

    # Filter by ID if provided
    if product_id is not None:
        filtered_products = [p for p in products if p['id'] == product_id]
        if not filtered_products:
            return render_template('product_display.html', error="Product not found")
        products = filtered_products

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
