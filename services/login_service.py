from flask import Blueprint, request, jsonify
# from route import app
from handler import login_handler
from utilities.validator import Validator
from utilities.authentication import config
import datetime, jwt
validateOBJ = Validator()

loginHandlerOBJ = login_handler.LoginHandler()

login = Blueprint('login', __name__)


@login.route('/login', methods=["POST"])
def signIn():
    #     Check credentials
    #     fetch data on the basis of username
    #     If success, create the token with user data and send
    try:
        credentials = request.get_json()
    except:
        return jsonify({'message': 'Enter valid username or password'}), 401
    try:
        username = str(credentials['username'])
    except:
        return jsonify({'message': 'Enter valid username or password'}), 401
    try:
        password = str(credentials['password'])
    except:
        return jsonify({'message': 'Enter valid username or password'}), 401

    fetcheddetails = loginHandlerOBJ.getUser(credentials)
    if fetcheddetails == False:
        return jsonify({'message': 'Invalid credentials'}), 401
    
    ### Create the JWT token and pass in the reponse to access further APIs ###
    token = jwt.encode({'username': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60 * 24)}, config)
    resp = jsonify({'token': token.decode('UTF-8'), "status_code": 200})
    return resp

