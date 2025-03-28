from flask import Flask, render_template, request
import webbrowser
from flask_sqlalchemy import SQLAlchemy

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
    
# Ensure the database is created
with app.app_context():
    db.create_all()

@app.route('/contact_list/', methods=['GET', 'POST'])
def booking_list():
    contact_list_data = Contact.query.all()

    if request.method == 'POST':
        query_name = request.form.get('query_name')
        query_email = request.form.get('email')
        query_occasion = request.form.get('query_occasion')

        if query_name:
            contact_list_data = [data for data in contact_list_data if query_name.lower() in 
                         (str(data.first_name).lower() + " " + str(data.last_name).lower())]

        if query_email:
            contact_list_data = [ data for data in contact_list_data if query_email.lower() in data.email ]

        if query_occasion:
            contact_list_data =[ data for data in contact_list_data if query_occasion.lower() in data.occasion.lower() ]

    return render_template('contact_list.html',contact_list_data=contact_list_data)

@app.route('/book_list/')
def contact_list():
    booking_list_data = Booking.query.all()
    return render_template('contact_list.html',booking_list_data=booking_list_data)



@app.route('/blog/')
def blog():
    return render_template('blog.html')

if __name__ == '__main__':
    webbrowser.open("http://127.0.0.1:5000/contact_list/")
    app.run(debug=True)
