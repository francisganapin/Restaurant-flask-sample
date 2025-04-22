from flask import Flask, render_template, request,url_for,redirect


import webbrowser
from flask_sqlalchemy import SQLAlchemy

from datetime import datetime

now = datetime.now()

#save this for our database contact
current_date = now.strftime("%m-%d-%y")
# save this as time for database contact 
current_time = now.strftime("%H:%M:%S")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Avoids a warning

db = SQLAlchemy(app)

<<<<<<< HEAD
class Booking(db.Model):
=======
class BookingTb(db.Model):
>>>>>>> a6e1b0b (4/22/2025)
    id = db.Column(db.Integer, primary_key=True)
    id_card = db.Column(db.String(27),nullable=False)
    select_date = db.Column(db.String(20))
    select_time = db.Column(db.String(20))
    status     = db.Column(db.String(20),nullable=False)

    def __repr__(self):
        return f'<Booking {self.select_date} {self.select_time}>'


<<<<<<< HEAD

class Contact(db.Model):
=======
class ContactTb(db.Model):
>>>>>>> a6e1b0b (4/22/2025)
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

#id card should valid before we can book 
@app.route('/home/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        select_id_card = request.form.get('select_id_card')
        select_date = request.form.get('select_date')
        select_time = request.form.get('select_time')
        status = 'Pending'

        if select_date and select_time:
<<<<<<< HEAD
            booking_data = Booking(select_date=select_date, 
=======
            booking_data = BookingTb(select_date=select_date, 
>>>>>>> a6e1b0b (4/22/2025)
                                   select_time=select_time,
                                   id_card=select_id_card,
                                   status=status
                                   )
            db.session.add(booking_data)
            db.session.commit()
            print("Booking saved:", select_date, select_time)

    return render_template('website_template/home.html')

@app.route('/recipe/')
def recipe():
    return render_template('website_template/recipe.html')

@app.route('/contact/',methods=['GET','POST'])
def contact():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email =  request.form.get('get_email')
        occasion = request.form.get('occasion')
        phone_number = request.form.get('phone_number')

<<<<<<< HEAD
        contact_data = Contact(first_name=first_name,
=======
        contact_data = ContactTb(first_name=first_name,
>>>>>>> a6e1b0b (4/22/2025)
                               last_name=last_name,
                               email=email,
                               occasion=occasion,
                               phone_number = phone_number,
                               time_input=current_time,
                               date_input=current_date

                               )
        db.session.add(contact_data)
        db.session.commit()
        
        print('Conctact save:',first_name,last_name,email,occasion,phone_number,current_time,current_date)
        return redirect(url_for('success',first_name=first_name,last_name=last_name,occasion=occasion))
    
    return render_template('website_template/contact.html')

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> a6e1b0b (4/22/2025)

@app.route('/contact/succes/')
def success():
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')
    occasion = request.args.get('occasion')

    print(f"Contact saved! Name:{first_name},{last_name} Occasion:{occasion} thank your for contact us")
    return render_template('website_template/success.html',first_name=first_name,last_name=last_name,occasion=occasion)
<<<<<<< HEAD
=======
    return render_template('website_template/contact.html')
>>>>>>> 1ccf7231c96113956d0a849f97e9948cc4ab5cec
=======
>>>>>>> a6e1b0b (4/22/2025)

@app.route('/blog/')
def blog():
    return render_template('blog.html')

if __name__ == '__main__':
<<<<<<< HEAD
<<<<<<< HEAD
    webbrowser.open("http://127.0.0.1:5000/home/")
    app.run(host='0.0.0.0', port=5000, debug=True)

=======
    app.run(debug=True)
    webbrowser.open("http://127.0.0.1:5000/home/")
    
>>>>>>> 1ccf7231c96113956d0a849f97e9948cc4ab5cec
=======
    webbrowser.open("http://127.0.0.1:5000/home/")
    app.run(host='0.0.0.0', port=5000, debug=True)

>>>>>>> a6e1b0b (4/22/2025)
