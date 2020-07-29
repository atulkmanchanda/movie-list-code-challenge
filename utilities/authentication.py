from functools import wraps
from flask import jsonify, request
import jwt

config = 'bdsfyvfvsify45458368%#$@@^kbgfkgdfkgk'


### Verify the user via JWT token ###
def token_req(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        try:
            if 'x-access-token' in request.headers:
                token = request.headers['x-access-token']
            if not token:
                return jsonify({'message': 'user is not authorised'}), 401
        except:
            return jsonify({'message': 'user is not authorised'}), 401

        try:
            ### Decode the token using secret key ###
            data = jwt.decode(token, config)
            if data['username'] == 'admin':
                current_user = 'admin'
            else:
                return jsonify({'message': 'Token is invalid!'}), 401

        except:
            return jsonify({'message': 'Token is invalid!'}), 401

        return f(current_user, *args, **kwargs)

    return decorated
