from flask import Flask, render_template, request
import webbrowser
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import flask_login






app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Avoids a warning

db = SQLAlchemy(app)

class Booking_Tb(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    select_date = db.Column(db.String(20))
    select_time = db.Column(db.String(20))

    def __repr__(self):
        return f'<Booking {self.select_date} {self.select_time}>'



class Contact_Tb(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    first_name = db.Column(db.String(20),nullable=False)
    last_name = db.Column(db.String(20),nullable=False)
    email = db.Column(db.String(45),nullable=False)
    occasion = db.Column(db.String(150),nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    time_input = db.Column(db.String(255),nullable=False)
    date_input = db.Column(db.String(255),nullable=False)

    def __repr__(self):
        return f'<Contact {self.first_name},{self.last_name}>'

class Stock_Tb(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(25),nullable=False)
    category = db.Column(db.String(25),nullable=False)
    quantity = db.Column(db.Integer,nullable=False)
    price = db.Column(db.Integer,nullable=False)

class Menu_Tb(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(55),nullable=False)
    category = db.Column(db.String(55),nullable=False)
    quantity = db.Column(db.Integer,nullable=False)
    price = db.Column(db.Integer,nullable=False)



class Customer_tb(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(25),nullable=False)
    orders = db.relationship('Order',backref='customer',lazy=True)

class Order(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    customer_id = db.Column(db.Integer,db.ForeignKey('customer_tb.id'),nullable=False)
    product = db.Column(db.String(100),nullable=False)
    amount = db.Column(db.Float,nullable=False)
    order_date = db.Column(db.String(100),nullable=False)

# Ensure the database is created
with app.app_context():
    db.create_all()




@app.route('/food_stock/',methods=['GET','POST'])
def food_list():
    stock_list_data = Stock_Tb.query.all()

    if request.method == 'POST':
        query_name = request.form.get('query_name')
        query_category = request.form.get('query_category')

        if query_name:
           stock_list_data = Stock_Tb.query.filter(Stock_Tb.name.ilike(f"%{query_name}%")).all()

        if query_category:
            if 'All' not in query_category:
                stock_list_data = Stock_Tb.query.filter(Stock_Tb.category == query_category).all()

    return render_template('owner_template/food_list.html',stock_list=stock_list_data)



@app.route('/contact_list/', methods=['GET', 'POST'])
def booking_list():
    contact_list_data = Contact_Tb.query.all()

    if request.method == 'POST':
        query_name = request.form.get('query_name')
        query_email = request.form.get('email')
        query_occasion = request.form.get('query_occasion')

        if query_name:
            contact_list_data = Contact_Tb.query
        if query_email:
            contact_list_data = [ data for data in contact_list_data if query_email.lower() in data.email ]

        if query_occasion:
            if "All" not in query_occasion:
                contact_list_data = [ data for data in contact_list_data if query_occasion in data.occasion]

    return render_template('owner_template/contact_list.html',contact_list_data=contact_list_data)




if __name__ == '__main__':
    webbrowser.open("http://127.0.0.1:5000/contact_list/")
    app.run(host='0.0.0.0', port=5000, debug=True)
