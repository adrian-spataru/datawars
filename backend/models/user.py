import datetime
from passlib.apps import custom_app_context as pwd_context
from db import db


class User(db.Model):
    """This class represents the users database table."""

    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), index=True, unique=True)
    password = db.Column(db.String(255), index=True, nullable=False)
    email = db.Column(db.String(255),unique=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    submissions = db.relationship("Submission", backref="user", lazy="dynamic")
    team_id = db.Column(db.Integer, db.ForeignKey("team.id"))

    def __init__(self, username, password):
        self.username = username
        self.password = self.hash_password(password)

    def hash_password(self, password):
        return pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password)
    
    @classmethod
    def find_by_username(cls,username):
        return cls.query.filter_by(username=username).first()

