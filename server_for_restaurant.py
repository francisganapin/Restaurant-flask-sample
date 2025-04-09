from flask import Flask, render_template, request,redirect,url_for,flash,get_flashed_messages
import webbrowser
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import flask_login






app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Avoids a warning

db = SQLAlchemy(app)

class BookingTb(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_card = db.Column(db.String(27),nullable=False)
    select_date = db.Column(db.String(20))
    select_time = db.Column(db.String(20))
    status     = db.Column(db.String(20),nullable=False)

    def __repr__(self):
        return f'<Booking {self.select_date} {self.select_time}>'



class ContactTb(db.Model):
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

class Food_stock(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(25),nullable=False,unique=True)
    category = db.Column(db.String(25),nullable=False)
    quantity = db.Column(db.Integer,nullable=False)
    price = db.Column(db.Integer,nullable=False)

class Customer_list(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    card_id = db.Column(db.String(25),nullable=False)
    first_name = db.Column(db.String(25),nullable=False)
    last_name = db.Column(db.String(25),nullable=False)
    email = db.Column(db.String(25),nullable=False)

#class Order(db.Model):
    #id = db.Column(db.Integer,primary_key=True)
    #customer_id = db.Column(db.Integer,db.ForeignKey('customer_list'),nullable=False)
    #product = db.Column(db.String(100),nullable=False)
    #amount = db.Column(db.Float,nullable=False)
    #order_date = db.Column(db.DateTime,default=datetime.utcnow)

# Ensure the database is created
with app.app_context():
    db.create_all()



@app.route('/register/',methods=['GET','POST'])
def register_customer():
    
    return render_template('owner_template/register_customer.html')






@app.route('/food_stock/',methods=['GET','POST'])
def food_list():

    page = request.args.get('page',1,type=int)

    query = Food_stock.query

    if request.method == 'POST':
        query_name = request.form.get('query_name', '').strip()
        query_category = request.form.get('query_category', '').strip()

        if  query_name:
            query = query.filter(Food_stock.name.ilike(f'%{query_name}%'))

       
        if query_category and query_category != 'All':
            query = query.filter_by(category=query_category)

    stock_list_data = query.paginate(page=page,per_page=6,error_out=False)

    return render_template('owner_template/food_list.html',stock_list=stock_list_data)

# add front end message handler  4/9/2025
@app.route('/food_stock/add/',methods=['GET','POST'])
def add_food_stock():
    message = ''
    if request.method == 'POST':
        try:
            name = request.form.get('food_name')
            category = request.form.get('food_category')
            quantity = request.form.get('food_quantity')
            price = request.form.get('food_price')

            print(name,category,quantity,price)

            new_food = Food_stock(name=name,
                                category=category,
                                quantity=quantity,
                                price=price)
            print(new_food)
            db.session.add(new_food)
            db.session.commit()
            flash('food was added succesfuly')
        except Exception as e:
            flash('sorry duplicate Name for Foods')
            print(f'name was duplicate sorry {e}')

    return redirect(url_for('food_list',message=message))




@app.route('/contact_list/', methods=['GET', 'POST'])
def booking_list():
    
    # set the page where we at
    page = request.args.get('page',1,type=int) 
    
    query = ContactTb.query

    if request.method == 'POST':
        query_name = request.form.get('query_name')
        query_email = request.form.get('query_email')
        query_occasion = request.form.get('query_occasion')

        print(query_name)
        result = query.all()
        print(result)

        if query_name:
            query = query.filter(
                db.or_(ContactTb.first_name.ilike(f'%{query_name}%'),
                ContactTb.last_name.ilike(f'%{query_name}%')
                ))
                
        if query_email:
            query = query.filter(
                ContactTb.email.ilike(f'%{query_email}%')
                )

        if query_occasion and query_occasion != 'All':
            contact_list_data = query.filter_by(occasion=query_occasion)
    
    contact_list_data = query.paginate(page=page,per_page=6,error_out=False)
    
    print(contact_list_data)
    return render_template('owner_template/contact_list.html',contact_list_data=contact_list_data)




if __name__ == '__main__':
    webbrowser.open("http://127.0.0.1:5000/contact_list/")
    app.run(host='0.0.0.0', port=5000, debug=True)
