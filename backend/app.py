from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from resources.accounts_manager import LoginResource, RegisterResource
from resources.competition import CompetitionsResource, CompetitionResource
from resources.team import TeamsResource, TeamResource 

app = Flask(__name__)
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
api.add_resource(CompetitionResource, '/competition/<string:url_code>')

# teams routes
api.add_resource(TeamsResource, '/teams')
api.add_resource(TeamResource, '/team/<string:team>')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
