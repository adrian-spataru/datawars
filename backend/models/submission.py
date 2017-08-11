import datetime
from passlib.apps import custom_app_context as pwd_context
from db import db


class Submission(db.Model):
    """This is class represents the submission database table."""

    __tablename__ = 'submission'

    id = db.Column(db.Integer, primary_key=True)
    competition_id = db.Column(db.Integer, db.ForeignKey("competition.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    submission = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    score = db.Column(db.Float)
    marked = db.Column(db.Boolean, default=False)

    def __init__(self, competition_id, user_id, submission, description, score):
        self.competition_id = competition_id
        self.user_id = user_id 
        self.description = description
        self.score = score
        self.submission = submission
