from flask import Flask, render_template, request
import json
import csv
import sqlite3


app = Flask(__name__)

def read_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        return []

def read_csv(file_path):
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
            # Convert price from string to float
            for item in data:
                item['price'] = float(item['price'])
            return data
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return []

def read_sqlite(db_path, product_id=None):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        if product_id:
            cursor.execute("SELECT id, name, category, price FROM Products WHERE id = ?", (product_id,))
        else:
            cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        conn.close()
        data = [{"id": row[0], "name": row[1], "category": row[2], "price": row[3]} for row in rows]
        return data
    except sqlite3.Error as e:
        print(f"Error reading SQLite database: {e}")
        return []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        data = read_json('products.json')
    elif source == 'csv':
        data = read_csv('products.csv')
    elif source == 'sql':
        data = read_sqlite('products.db', product_id)
    else:
        return render_template('product_display.html', error="Wrong source")

    if product_id:
        product_id = int(product_id)
        data = [product for product in data if product['id'] == product_id]
        if not data:
            return render_template('product_display.html', error="Product not found")
    
    return render_template('product_display.html', products=data)

@app.route('/items')
def items():
    data = read_json('items.json')
    items = data.get('items', [])
    return render_template('items.html', items=items)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
