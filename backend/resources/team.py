import logging
from flask import jsonify, make_response
from flask_restful import Resource, reqparse, fields, marshal

from models.user import User 
from models.team import Team 
from utils.db import save_record, delete_record
from utils.auth.authorize import login_required

logger = logging.getLogger(__name__)

team_field = {
                        "id": fields.Integer,
                        "name": fields.String,
                        "created_at": fields.DateTime,
                    }


class TeamsResource(Resource):
    """ this class gets all the teams in the database."""

    @login_required
    def get(self,user_id=None, response=None):
        if user_id is not None:
            team_all = Team.query.all()
            if team_all:
                return marshal(team_all, team_field), 200
            response = ("No teams found.", 409)
        return make_response(jsonify({
            "message": response[0]
        }), response[1])


class TeamResource(Resource):
    """ this class deals with a single team in the database."""
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("name",
                                 type=str,
                                 required=True,
                                 help="Name of the team is required",
                                 location="json")

    @login_required
    def get(self, team=None, user_id=None, response=None):
        if user_id is not None:
            if team is not None:
                if Team.query.filter_by(name=team).first():
                    return marshal(Team.query.filter_by(name=team).first(), team_field), 200
                response = ("Team not found.", 409)
        return make_response(jsonify({
            "message": response[0]
        }), response[1])


    @login_required
    def post(self, team=None, user_id=None, response=None):
        args = self.parser.parse_args()
        name = args["name"]
        if user_id is not None:

            if Team.query.filter_by(name=name).first():
                response = ("Team with a similar name exists", 409)
            else:
                team = Team(name)
                data = save_record(team)
                response = ("Team %s created successfully" % name, 201)

        return make_response(jsonify({
            "message": response[0]
        }), response[1])

class AssignTeamResource(Resource):
    """ this class deals with assigning members to teams in the database."""

    @login_required
    def post(self, team=None, user_id=None, response=None):
        if user_id is not None:
            value =Team.query.filter_by(name=team).first() 
            if value:
                user = User.query.filter_by(id=user_id).first()
                user.team_id = value.id
                save_record(user)
                response = ("Assigned User to Team %s successfully" % team, 201)
            else:
                response = ("Team %s not found" % team, 201)

        return make_response(jsonify({
            "message": response[0]
        }), response[1])

