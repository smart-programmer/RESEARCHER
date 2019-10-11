from RESEARCHER import db, login_manager
from flask_login import UserMixin
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(500), nullable=False)
    researches = db.relationship('Researche', backref="product", lazy='dynamic', foreign_keys = 'Product.user_id')
    
    def __repr__(self):
        return f"{self.full_name}"



class Researche(db.Model):
    id = db.Column(db.Integer, primary_key=True)    
    def __repr__(self):
        return f"{self.id}