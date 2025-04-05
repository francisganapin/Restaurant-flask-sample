from flask import Flask, render_template, request
import webbrowser
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import flask_login






app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Avoids a warning

db = SQLAlchemy(app)

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    select_date = db.Column(db.String(20))
    select_time = db.Column(db.String(20))

    def __repr__(self):
        return f'<Booking {self.select_date} {self.select_time}>'



class Contact(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    first_name = db.Column(db.String(20),nullable=False)
    last_name = db.Column(db.String(20),nullable=False)
    email = db.Column(db.String(45),nullable=False)
    occasion = db.Column(db.String(150),nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    time_input = db.Column(db.String(255),nullable=False)
    date_input = db.Column(db.String(255),nullable=False)
    def __repr__(self):
        return f'<Contact {self.name}>'

class Food_stock(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(25),nullable=False)
    category = db.Column(db.String(25),nullable=False)
    quantity = db.Column(db.Integer,nullable=False)
    price = db.Column(db.Integer,nullable=False)

#class Customer_list(db.Model):
    #id = db.Column(db.Integer,primary_key=True)
    #name = db.Column(db.String(25),nullable=False)
    #orders = db.relationship('Order',backref='customer',lazy=True)
#class Order(db.Model):
    #id = db.Column(db.Integer,primary_key=True)
    #customer_id = db.Column(db.Integer,db.ForeignKey('customer_list'),nullable=False)
    #product = db.Column(db.String(100),nullable=False)
    #amount = db.Column(db.Float,nullable=False)
    #order_date = db.Column(db.DateTime,default=datetime.utcnow)

# Ensure the database is created
with app.app_context():
    db.create_all()




@app.route('/food_stock/',methods=['GET','POST'])
def food_list():
    stock_list_data = Food_stock.query

    if request.method == 'POST':
        query_name = request.form.get('query_name', '').strip()
        query_category = request.form.get('query_category', '').strip()

        if  query_name:
            stock_list_data = stock_list_data.filter(Food_stock.name.ilike(f'%{query_name}%'))

       
        if query_category and query_category != 'All':
            stock_list_data = stock_list_data.filter_by(category=query_category)
       



    return render_template('owner_template/food_list.html',stock_list=stock_list_data)



@app.route('/contact_list/', methods=['GET', 'POST'])
def booking_list():
    contact_list_data = Contact.query.all()

    if request.method == 'POST':
        query_name = request.form.get('query_name')
        query_email = request.form.get('email')
        query_occasion = request.form.get('query_occasion')

        if query_name:
            contact_list_data = [
                
                

        if query_email:
            contact_list_data = [ data for data in contact_list_data if query_email.lower() in data.email ]

        if query_occasion:
            if "All" not in query_occasion:
                contact_list_data = [ data for data in contact_list_data if query_occasion in data.occasion]

    return render_template('owner_template/contact_list.html',contact_list_data=contact_list_data)




if __name__ == '__main__':
    webbrowser.open("http://127.0.0.1:5000/contact_list/")
    app.run(host='0.0.0.0', port=5000, debug=True)
