from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Ambientvalues(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    humidity = db.Column(db.REAL())
    objtemp = db.Column(db.REAL())
    ambtemp = db.Column(db.REAL())
    illuminance = db.Column(db.REAL())
    timestamp = db.Column(db.TEXT(64))
    epoch = db.Column(db.INTEGER)

    def __repr__(self):
        return '<Ambiente %r>' % (self.id)
