import logging
from flask import jsonify, make_response
from flask_restful import Resource, reqparse, fields, marshal

from models.user import User 
from models.competition import Competition 
from models.submission import Submission 
from utils.db import save_record, delete_record
from utils.auth.authorize import login_required

logger = logging.getLogger(__name__)

submission_field = {
                        "id": fields.Integer,
                        "competition_id": fields.Integer,
                        "user_id": fields.Integer,
                        "submission": fields.String,
                        "description": fields.String,
                        "created_at": fields.DateTime,
                        "public_score": fields.Float,
                        "private_score": fields.Float,
                        "marked": fields.Boolean,
                    }


class SubmissionsResource(Resource):
    """ this class gets all the submissions in the database."""

    @login_required
    def get(self,comp_id=None,user_id=None, response=None):

        if user_id and comp_id is not None:
            submissions_all = Submission.query.filter_by(competition_id=comp_id).all()
            if submissions_all:
                return marshal(submissions_all, submission_field), 200
            response = ("No Submissions found.", 409)
        return make_response(jsonify({
            "message": response[0]
        }), response[1])


class SubmissionResource(Resource):
    """ this class deals with single submission in the database."""
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("submission",
                                 type=str,
                                 required=True,
                                 help="Submission is required",
                                 location="json")

    @login_required
    def get(self, comp_id=None, user_id=None, response=None):
        if user_id and comp_id is not None:
            if Submission.query.filter_by(competition_id=comp_id).filter_by(user_id=user_id).all():
                return marshal(Submission.query.filter_by(competition_id=comp_id).filter_by(user_id=user_id).all(), submission_field), 200
            response = ("Submissions not found.", 409)
        return make_response(jsonify({
            "message": response[0]
        }), response[1])


    @login_required
    def post(self, comp_id=None, user_id=None, response=None):
        args = self.parser.parse_args()
        submission = args["submission"]
        
        if comp_id and user_id is not None:
            #TODO: Implement Score evaluation.
            submission = Submission(comp_id, user_id, submission, "Submission", -1.0, -1.0)
            data = save_record(submission)
            response = ("Submission created successfully", 201)

        return make_response(jsonify({
            "message": response[0]
        }), response[1])

