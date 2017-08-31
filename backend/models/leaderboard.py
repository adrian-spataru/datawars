from db import db

class Leaderboard(db.Model):
    """This class represents the metadata of a leaderboard database table."""

    __tablename__ = "leaderboard"

    id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.Integer, db.ForeignKey("team.id"))
    competition_id = db.Column(db.Integer, db.ForeignKey("competition.id"))
    submission_id = db.Column(db.Integer, db.ForeignKey("submission.id"))
    entries_counts = db.Column(db.Integer, default=0)
    public_trend_place = db.Column(db.Integer)
    private_trend_place = db.Column(db.Integer)
    # if trend: 0=hasn't changed; 1=positive; -1=negative
    # TODO: USE ENUM INSTEAD
    trend = db.Column(db.Integer, default=0)



    def __init__(self, team_id, competition_id, submission_id= None, entries_counts= None, public_trend_place= None, private_trend_place= None, trend= None):
        self.team_id = team_id
        self.competition_id = competition_id
        self.submission_id = submission_id
        self.public_trend_place = public_trend_place
        self.private_trend_place = private_trend_place

        if trend:
            self.trend = trend
        if entries_counts:
            self.entries_counts = entries_counts
        
