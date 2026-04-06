from flask import Flask, render_template, request, redirect

app = Flask(__name__)

products = []
transactions = []

@app.route('/')
def index():
    search = request.args.get('search')
    if search:
        filtered = [p for p in products if search.lower() in p['category'].lower()]
    else:
        filtered = products
    return render_template('index.html', products=filtered)

@app.route('/add', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name = request.form['name']
        category = request.form['category']
        price = request.form['price']
        product = {'name': name, 'category': category, 'price': price}
        products.append(product)
        return redirect('/')
    return render_template('add_product.html')

@app.route('/buy/<int:index>')
def buy(index):
    product = products.pop(index)
    transactions.append(product)
    return redirect('/transactions')

@app.route('/transactions')
def transaction_history():
    return render_template('transactions.html', transactions=transactions)

if __name__ == '__main__':
    app.run(debug=True)
