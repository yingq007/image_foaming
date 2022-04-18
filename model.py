"""Models for images foaming"""

from flask_sqlalchemy import SQLAlchemy
import os


db= SQLAlchemy()

class User(db.Model):
    """A user."""

    __tablename__="users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String)
    images = db.relationship("Image", backref="users")
    
    def __repr__(self):
        return f"<User user_id={self.user_id} email={self.email}>"


class Image(db.Model):
    """An image"""

    __tablename__="images"

    image_id=db.Column(db.Integer,autoincrement=True, primary_key=True)
    url = db.Column(db.String)
    lastModified=db.Column(db.String)
    foam = db.Column(db.String)
    user_id=db.Column(db.Integer, db.ForeignKey("users.user_id"))

    
    def __repr__(self):
        return f"<Image image_id={self.image_id} url={self.url} lastModified={self.lastModified}>"



def connect_to_db(flask_app, db_uri='postgresql:///foams', echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"]= db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    

    db.app=flask_app
    db.init_app(flask_app)
    print("Connected to the db!")

if __name__=="__main__":
    from server import app

    connect_to_db(app)


    
