import unittest

from app import app


### Created the Base class to setup unit test ###
class BaseCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
