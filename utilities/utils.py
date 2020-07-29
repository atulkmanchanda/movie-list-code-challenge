import json
import os

# __file__ = 'utils'
dirname = os.path.dirname(__file__)
APP_DATA_PATH = os.path.join(dirname, 'data.json')

class Utils:
    def __init__(self):
        print('values')

    ### Read the json file to retrieve the movies list data ###
    def getApplicationData(self):
        status_message = "Fetching Application Data"
        print(status_message)
        json_file = open(APP_DATA_PATH, 'r').read()
        app_data = json.loads(json_file)
        return app_data

    ### Write the json file to save the new added movies data ###
    def writeApplicationData(self, data):
        with open(APP_DATA_PATH, 'w') as outfile:
            json.dump(data, outfile)
            return data
    