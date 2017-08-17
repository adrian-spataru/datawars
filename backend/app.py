from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from resources.accounts_manager import LoginResource, RegisterResource
from resources.competition import CompetitionsResource, CompetitionResource
from resources.submission import SubmissionsResource, SubmissionResource 
from resources.leaderboard import PublicLeaderboardResource, PrivateLeaderboardResource
from resources.team import TeamsResource, TeamResource, AssignTeamResource
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, resources={r'/*': {"origins": '*'}})
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'Random Tree Random Forest'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()


# login routes
api.add_resource(RegisterResource, '/auth/register')
api.add_resource(LoginResource, '/auth/login')

# competition routes
api.add_resource(CompetitionsResource, '/competitions')
api.add_resource(CompetitionResource, '/competition/<int:comp_id>','/competition', '/competition/')

# submissions routes
api.add_resource(SubmissionsResource, '/competition/<int:comp_id>/submissions/','/competition/<int:comp_id>/submissions')

api.add_resource(SubmissionResource, '/competition/<int:comp_id>/submission/', '/competition/<int:comp_id>/submission')

# leaderboard routes
api.add_resource(PublicLeaderboardResource, '/competition/<int:comp_id>/public_leaderboard/')
api.add_resource(PrivateLeaderboardResource, '/competition/<int:comp_id>/private_leaderboard/')

# teams routes
api.add_resource(TeamsResource, '/teams','/teams/')
api.add_resource(TeamResource, '/team/<string:team>','/team/','/team')
api.add_resource(AssignTeamResource, '/assignteam/<string:team>')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
