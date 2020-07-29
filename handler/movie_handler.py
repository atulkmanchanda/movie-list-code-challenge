from utilities.utils import Utils
import json

UTILSOBJ = Utils()

class MovieHandler:
    __data = None
    ### Get the movies list data stored in json file ###
    def __init__(self):
        self.__data = UTILSOBJ.getApplicationData()

    ### Iterate the data in view format ###
    def getMovies(self):
        data = self.__data
        new_data = {}
        serialize = list(data['movies'][0].values())
        new_data['movies'] = serialize
        return new_data

    ### Save the movie data in the json file ###
    def saveMovie(self, data):
        print(data)
        try:
            new_title = data['title']
            self.__data['movies'][0][new_title] = data
            ### Write the data in file ###
            UTILSOBJ.writeApplicationData(self.__data)
            return {"movieName":data['title'],"message": "Movie added successfully"}
        except Exception as E:
            print(str(E))
            raise Exception("Something went wrong")

    ### Delete the movie data from the json file ###
    def deleteMovie(self, input):
        data = self.__data
        try:
            titleToDel = input['title']
            ### If the passed key not present ###
            if titleToDel not in data['movies'][0]:
                return {"movieName":input['title'],"message": False}
            del data['movies'][0][titleToDel]

            ### Write the data in file ###
            UTILSOBJ.writeApplicationData(data)
            return {"movieName":input['title'],"message": "Movie removed successfully"}
        except Exception as E:
            print(str(E))
            raise Exception("Something went wrong")

    
    ### Delete the movie from the json file ###
    def updateMovie(self, input):
        data = self.__data
        try:
            key = input['title']
            movieData = data['movies'][0]
            movieData[key] = input
            ### Write the data in file ###
            UTILSOBJ.writeApplicationData(data)
            return {"movieName":input['title'],"message": "Movie updated successfully"}
        except Exception as E:
            print(str(E))
            raise Exception("Something went wrong")
