import logging
from flask import jsonify, make_response
from flask_restful import Resource, reqparse, fields, marshal

from models.user import User 
from models.competition import Competition 
from models.submission import Submission 
from utils.db import save_record, delete_record
from utils.auth.authorize import login_required

logger = logging.getLogger(__name__)

public_leaderboard_fields = {
                        "id": fields.Integer,
                        "competition_id": fields.Integer,
                        "user_id": fields.Integer,
                        "submission": fields.String,
                        "description": fields.String,
                        "created_at": fields.DateTime,
                        "public_score": fields.Float,
                        "marked": fields.Boolean,
                        "team_name": fields.String(attribute=lambda x: x.user.team.name)
                    }
private_leaderboard_fields = {
                        "id": fields.Integer,
                        "competition_id": fields.Integer,
                        "user_id": fields.Integer,
                        "submission": fields.String,
                        "description": fields.String,
                        "created_at": fields.DateTime,
                        "public_score": fields.Float,
                        "private_score": fields.Float,
                        "marked": fields.Boolean,
                        "team_name": fields.String(attribute=lambda x: x.user.team.name)
                    }


class PublicLeaderboardResource(Resource):
    """ this class deals with the public leaderboard in the database."""
    
    """
    GET /competition/<int: user_id>/public_leaderboard
    This returns the public leaderboard of a competition
    """
    @login_required
    def get(self,comp_id=None,user_id=None, response=None):
        if user_id and comp_id is not None:
            # TODO: This is very bad and you should be ashamed. Grab the db session to make the query. Active Record is a bit limited.
            submissions_all = Submission.query.filter_by(competition_id=comp_id).order_by(Submission.score).all() # DON'T USE ORDER_BY IF YOU AVOID IT
            if submissions_all:
                user_sub_map = {}
                for s in submissions_all:
                    user_sub_map[s.user.team_id] = s
                submissions_all = [x[1] for x in user_sub_map.items()]
                return marshal(submissions_all, public_leaderboard_fields), 200
            response = ("No Submissions found.", 409)

        return make_response(jsonify({
            "message": response[0]
        }), response[1])


class PrivateLeaderboardResource(Resource):
    """ this class deals with the private leaderboard in the database."""
    
    """
    GET /competition/<int: user_id>/private_leaderboard
    This returns the private leaderboard of a competition
    """
    @login_required
    def get(self,comp_id=None,user_id=None, response=None):
        if user_id and comp_id is not None:
            # TODO: This is very bad and you should be ashamed. Grab the db session to make the query. Active Record is a bit limited.
            submissions_all = Submission.query.filter_by(competition_id=comp_id).order_by(Submission.score).all() # DON'T USE ORDER_BY IF YOU AVOID IT
            if submissions_all:
                user_sub_map = {}
                for s in submissions_all:
                    user_sub_map[s.user.team_id] = s
                submissions_all = [x[1] for x in user_sub_map.items()]
                return marshal(submissions_all, private_leaderboard_fields), 200
            response = ("No Submissions found.", 409)

        return make_response(jsonify({
            "message": response[0]
        }), response[1])

