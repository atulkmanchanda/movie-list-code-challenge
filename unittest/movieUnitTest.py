import unittest
from app import app
from BaseClass import BaseCase
import json

class MovieTest(BaseCase):
    def setUp(self):
        self.app = app.test_client()
        self.url = '127.0.0.1/movie'

    ### Test the post method request ###
    def test_successful_post(self):
        # Given
        payload = json.dumps({
            "productionCompany": "Meri movies",
            "releaseDate": "22-Jan",
            "title": "1 movie"
        })

        # When
        response = self.app.post(self.url, headers={"Content-Type": "application/json"}, data=payload)
        print(response.status_code)
        # Then
        self.assertEqual(201, response.status_code)

    ### Test the get method request ###
    def test_successful_get(self):
        # when
        response = self.app.get(self.url, headers={"Content-Type": "application/json"})
        print(response.status_code)
        # Then
        self.assertEqual(200, response.status_code)

    ### Test the put method request ###
    def test_successful_put(self):
        payload = json.dumps({
            "productionCompany": "Meri movies",
            "releaseDate": "22-Jan",
            "title": "1 movie"
        })
        # When
        response = self.app.put(self.url, headers={"Content-Type": "application/json"}, data=payload)
        print(response.status_code)
        # Then
        self.assertEqual(200, response.status_code)

    ### Test the delete method request ###
    def test_successful_delete(self):
        payload = json.dumps({
            "productionCompany": "Meri movies",
            "releaseDate": "22-Jan",
            "title": "1 movie"
        })
        #When
        response = self.app.delete(self.url, headers={"Content-Type": "application/json"}, data=payload)
        print(response.status_code)
        # Then
        self.assertEqual(200, response.status_code)

