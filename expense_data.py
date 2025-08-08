from datetime import date
from server_for_restaurant import Expense,db,app


with app.app_context():
    expense1 = Expense(name='Groceries',amount=1200.50,date=date(2025,8,8))
    expense2 = Expense(name='Gas Refill',amount=800.00,date=date(2025,8,7))

    db.session.add_all([expense1,expense2])
    db.session.commit() 