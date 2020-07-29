from flask import Blueprint, request, jsonify
from handler import movie_handler
from utilities.validator import Validator
from utilities.authentication import token_req, config

validateOBJ = Validator()

movieHandlerOBJ = movie_handler.MovieHandler()

movie = Blueprint('movie', __name__)


@movie.route('/movie', methods=["POST","GET","PUT","DELETE"])
@token_req
def addMovie(current_user):
    try:
        ### Identify the request method and call the particular function in the handler file ###
        if request.method == 'POST':
            try:
                res = validateOBJ.ValidateRequest(request.get_json())
            except Exception as E:
                return jsonify({'message': 'Input invalid'}), 400
            if res is not True:
                return jsonify({'message': res}), 400
            request_data = request.get_json()
            details = movieHandlerOBJ.saveMovie(request_data)
            return jsonify({'movie': details['movieName'],'message': details['message']}), 201

        elif request.method == 'GET':
            val = movieHandlerOBJ.getMovies()
            return jsonify({'data':val})

        elif request.method == 'PUT':
            try:
                res = validateOBJ.ValidateRequest(request.get_json())
            except Exception as E:
                return jsonify({'message': 'Input invalid'}), 400
            if res is not True:
                return jsonify({'message': res}), 400
            request_data = request.get_json()
            details = movieHandlerOBJ.updateMovie(request_data)
            return jsonify({'movie': details['movieName'],'message': details['message']}), 200

        elif request.method == 'DELETE':
            try:
                res = validateOBJ.ValidateDelRequest(request.get_json())
            except Exception as E:
                return jsonify({'message': 'Input invalid'}), 400
            if res is not True:
                return jsonify({'message': res}), 400
            request_data = request.get_json()
            details = movieHandlerOBJ.deleteMovie(request_data)
            if details['message'] is False:
                return jsonify({'message': 'Movie not found'}), 400
            return jsonify({'movie': details['movieName'],'message': details['message']}), 200

        else:
            return jsonify({'message': 'Method not valid'}), 400
    except Exception as E:
        print(str(E))
        return jsonify({'message': str(E)}), 500

