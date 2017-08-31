from db import db


class TeamUser(db.Model):
    """This class maps users to teams in a database table."""

    __tablename__ = "team_user"

    id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.Integer, db.ForeignKey("team.id"), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
    teams = db.relationship("Team", back_populates="users")
    users = db.relationship("User", back_populates="teams")

    def __init__(self, team_id, user_id):
        self.team_id = team_id
        self.user_id = user_id
  

