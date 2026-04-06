from chatbot import db,app,login_manager
from flask_login import UserMixin
from sqlalchemy import ForeignKey

@login_manager.user_loader
def load_user(id):
    return Register.query.get(int(id))

class Register(db.Model, UserMixin):
    id=db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    address= db.Column(db.String (80))
    email= db.Column(db.String(80))
    contact= db.Column(db.String (10))
    password = db.Column(db.String(80))
    admission_no = db.Column(db.String(80))
    course = db.Column(db.String(80))
    usertype = db.Column(db.String(80))






   


 





