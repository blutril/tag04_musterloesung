from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the TechStyle E-Commerce Application!"

@app.route('/products')
def product_listing():
    return "Here is a list of products."

if __name__ == '__main__':
    app.run(debug=True)