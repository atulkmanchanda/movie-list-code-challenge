class Validator:
    __postData = ["title", "releaseDate", "productionCompany"]
    __delData = ["title"]

    ### To validate the POST, PUT request json ###
    def ValidateRequest(self, request):
        keys = [x for x in self.__postData if x not in request]
        if len(keys) > 0:
            keys = ', '.join(keys)
            return (keys + ' missing')
        else:
            return True

    ### To validate the Delete request json ###
    def ValidateDelRequest(self, request):
        keys = [x for x in self.__delData if x not in request]
        if len(keys) > 0:
            keys = ', '.join(keys)
            return (keys + ' missing')
        else:
            return True
