from flask import Flask,request, jsonify
from services import movie_service, login_service
from flask_cors import CORS
app = Flask(__name__)
cors = CORS(app)

### Registering blueprints ###
app.register_blueprint(movie_service.movie)
app.register_blueprint(login_service.login)
