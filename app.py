from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
# from send_mail import send_mail
app = Flask(__name__)

ENV = 'prod'

#  Access Production Database
# heroku run python
# from app import db
# db.create_all()
# exit()
# heroku pg:psql --app acumealio
if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost/acumeal_landingpage'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://zeojgfjosbblkd:499f3802efeceb978b73be2b6f67fedbf56ae476822976c661973bfb140bd6f1@ec2-54-152-175-141.compute-1.amazonaws.com:5432/d7f3785mc2ho0m'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
# Access Local Database
# from app import db
# db.create_all()
# exit()
# run your server and use database on website locally
class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    first = db.Column(db.String(200), unique=True)
    last = db.Column(db.String(200), unique=True)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(200), unique=True)
    email = db.Column(db.String(200), unique=True)
    number = db.Column(db.Integer)


    def __init__(self, first, last, age, gender, email, number):
        self.first = first
        self.last = last
        self.age = age
        self.gender = gender 
        self.email = email
        self.number = number


@app.route('/')
def index():
    return render_template('index.html')



@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        first = request.form['first']
        last = request.form['last']
        age = request.form['age']
        gender = request.form['gender']
        email = request.form['email']
        number = request.form['number']
        if first == '' or email == '':
            return render_template('index.html', message='Please enter required fields')

        if db.session.query(Feedback).filter(Feedback.email == email).count() == 0:
            data = Feedback(first, last, age, gender, email, number)
            db.session.add(data)
            db.session.commit()
            # send_mail(first, last, email)
            return render_template('success.html')
        return render_template('index.html', message='You have already been added to the waitlist')

if __name__ == '__main__':
    app.run(debug=True)