from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Restaurant(db.Model):
    __tablename__ = 'Restaurant'

    id = db.Column(db.Integer, primary_key=True)

# add any models you may need. 
class Restaurant(db.Model):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)  # Restaurant name