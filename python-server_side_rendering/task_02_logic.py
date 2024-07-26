from flask import Flask, render_template
import json

app = Flask(__name__)

def read_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except Exception as e:
        print(f"Error reading JSON file: {e}")
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

@app.route('/items')
def items():
    data = read_json('items.json')
    items = data.get('items', [])
    return render_template('items.html', items=items)


if __name__ == '__main__':
    app.run(debug=True, port=5000)