# Import libraries
from flask import Flask, request, url_for, redirect, render_template

# Instantiate Flask functionality
app = Flask(__name__)

# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300},
    {'id': 4, 'date': '2023-06-04', 'amount': -50},
    {'id': 5, 'date': '2023-06-05', 'amount': 150},
    {'id': 6, 'date': '2023-06-06', 'amount': -100},
    {'id': 7, 'date': '2023-06-07', 'amount': 200},
    {'id': 8, 'date': '2023-06-08', 'amount': -250},
    {'id': 9, 'date': '2023-06-09', 'amount': 350},
    {'id': 10, 'date': '2023-06-10', 'amount': -150},
    {'id': 11, 'date': '2023-06-11', 'amount': 120},
    {'id': 12, 'date': '2023-06-12', 'amount': -180},
    {'id': 13, 'date': '2023-06-13', 'amount': 220},
    {'id': 14, 'date': '2023-06-14', 'amount': -300},
    {'id': 15, 'date': '2023-06-15', 'amount': 180},
    {'id': 16, 'date': '2023-06-16', 'amount': -90},
    {'id': 17, 'date': '2023-06-17', 'amount': 250},
    {'id': 18, 'date': '2023-06-18', 'amount': -200},
    {'id': 19, 'date': '2023-06-19', 'amount': 400},
    {'id': 20, 'date': '2023-06-20', 'amount': -120},
    {'id': 21, 'date': '2023-06-21', 'amount': 300},
    {'id': 22, 'date': '2023-06-22', 'amount': -350},
    {'id': 23, 'date': '2023-06-23', 'amount': 180},
    {'id': 24, 'date': '2023-06-24', 'amount': -220},
    {'id': 25, 'date': '2023-06-25', 'amount': 150}
]

# Total Balance
@app.route('/balance')
def total_balance():
    # Calculate total balance
    total_balance = sum(transaction['amount'] for transaction in transactions)

    # Render balance template passing total_balance
    return total_balance

# Read operation
@app.route('/')
def get_transactions():
    # Get the balance total
    balance = total_balance

    # Render the transactions template with transactions and total balance
    return render_template('transactions.html', transactions=transactions, total_balance=balance)

# Create operation
@app.route('/add', methods=['GET', 'POST'])
def add_transaction():
    if request.method == 'POST':
        # Create a new transaction
        transaction = {
            'id': len(transactions) + 1,
            'date': request.form['date'],
            'amount': request.form['amount']
        }

        # Add the transaction to the transactions
        transactions.append(transaction)

        # Redirect to the transactions page list
        return redirect(url_for('get_transactions'))
    
    # Render the form template to display the add transactions form
    return render_template('form.html')

# Update operation
@app.route('/edit/<int:transaction_id>', methods=['GET', 'POST'])
def edit_transaction(transaction_id):
    if request.method == 'POST':
        # Extract the update values from the html input
        date = request.form['date']
        amount = request.form['amount']

        # Find the transaction with the matching ID and update it
        for transaction in transactions:
            if transaction['id'] == transaction_id:
                transaction['date'] = date
                transaction['amount'] = amount
                break

        # Redirect to the transactions list page
        return redirect(url_for("get_transactions"))
    
    # Find the transaction with the matching ID and display the update form
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            return render_template('edit.html', transaction=transaction)

# Delete operation
@app.route('/delete/<int:transaction_id>')
def delete_transaction(transaction_id):
    # Find the transaction with the matching ID and remove it
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            transactions.remove(transaction)
            break
    # Redirect to the transactions list page
    return redirect(url_for("get_transactions"))


# Search transactions
@app.route('/search', methods=['GET', 'POST'])
def search_transactions():
    if request.method == 'POST':

        # Extract the minimum and maximum amount from the form data
        minimum_amount = float(request.form['min_amount'])
        maximum_amount = float(request.form['max_amount'])

        # Create an empty list to store the filtered transactions
        filtered_transactions = []

        for transaction in transactions:
            if minimum_amount <= transaction['amount'] <= maximum_amount:
                filtered_transactions.append(transaction)

        # Render the transactions in a list
        return render_template('transactions.html', transactions=filtered_transactions)
        
    # Render the search form for GET request
    return render_template('search.html')

    

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)