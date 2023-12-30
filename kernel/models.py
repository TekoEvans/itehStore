from email.policy import default
from enum import unique
from app import db
from datetime import datetime
import json
from os.path import exists

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)
    published = db.Column(db.Integer, default=0)
    images = db.Column(
        db.Text, 
        nullable=False, 
        default=json.dumps({
            'main' : 'img/default.svg',
            'one' : 'img/default.svg',
            'two' : 'img/default.svg',
            'three' : 'img/default.svg',
            'four' : 'img/default.svg',
            'five' : 'img/default.svg',
            'six' : 'img/default.svg',
        })
    )
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    def getImage(self, name):
        return json.loads(self.images)[name]

    def getPrice(self):
        return int(self.price)

    def notPublished(self):
        return self.published == 0

    def hasNoReleatedImages(self):
        return json.loads(self.images) == {'main' : 'img/products/'+ str(self.id) +'/main.png','one' : 'img/default.svg','two' : 'img/default.svg','three' : 'img/default.svg','four' : 'img/default.svg','five' : 'img/default.svg','six' : 'img/default.svg'}

class Subscriber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)

def init_db():
    db.create_all()

if __name__ == "__main__":
    init_db()
    db.session.commit()