import logging
from flask import jsonify, make_response
from flask_restful import Resource, reqparse, fields, marshal

from models.user import User 
from models.competition import Competition 
from utils.db import save_record, delete_record
from utils.auth.authorize import login_required

logger = logging.getLogger(__name__)

competition_field = {
                        "id": fields.Integer,
                        "name": fields.String,
                        "description": fields.String,
                        "data": fields.String,
                        "created_at": fields.DateTime,
                        "ending_at": fields.DateTime,
                    }


class CompetitionsResource(Resource):
    """ this class gets all the competitions in the database."""

    @login_required
    def get(self,user_id=None, response=None):
        if user_id is not None:
            competitions_all = Competition.query.all()
            if competitions_all:
                return marshal(competitions_all, competition_field), 200
            response = ("No competitions found.", 409)
        return make_response(jsonify({
            "message": response[0]
        }), response[1])


class CompetitionResource(Resource):
    """ this class deals with single competition in the database."""
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("name",
                                 type=str,
                                 required=True,
                                 help="Name of the competition is required",
                                 location="json")

        self.parser.add_argument("description",
                                 type=str,
                                 required=True,
                                 help="Competition description is required",
                                 location="json")

        self.parser.add_argument("data",
                                 type=str,
                                 required=True,
                                 help="Competition data description/source is required",
                                 location="json")

        self.parser.add_argument("ending_at", type=int,location="json")

    @login_required
    def get(self, url_code=None, user_id=None, response=None):
        if user_id is not None:
            if url_code is not None:
                if Competition.query.filter_by(url_code=url_code).first():
                    return marshal(Competition.query.filter_by(url_code=url_code).first(), competition_field), 200
                response = ("Competition not found.", 409)
        return make_response(jsonify({
            "message": response[0]
        }), response[1])


    @login_required
    def post(self, url_code=None, user_id=None, response=None):
        args = self.parser.parse_args()
        name = args["name"]
        description = args["description"]
        data = args["data"]
        if user_id is not None:

            if Competition.query.filter_by(url_code=url_code).first():
                response = ("Competition with a similar name exists", 409)
            else:
                competition = Competition(name, url_code, description, data)
                data = save_record(competition)
                response = ("Competition created successfully", 201)

        return make_response(jsonify({
            "message": response[0]
        }), response[1])

