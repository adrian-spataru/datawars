import datetime
from db import db

class Team(db.Model):
    """This class represents the users database table."""

    __tablename__ = "team"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), index=True, unique=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    users = db.relationship("User", backref="team", lazy="dynamic")

    def __init__(self, name)
        self.name = name
