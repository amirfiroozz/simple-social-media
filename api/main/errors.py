
class Error:
    def __init__(self , msg , status) -> None:
        self.msg = msg
        self.status = status
    
    def responseData(self):
        return {
            "error":self.msg
        }
    
    def responseStatus(self):
        return self.status
    
    @staticmethod
    def postNotFoundedError():
        return newError("post not founded" , 404)
    @staticmethod
    def userNotFoundedError():
        return newError("user not founded" , 404)
    @staticmethod
    def alreayLikedError():
        return newError("alreay liked" , 409)
    @staticmethod
    def internalError():
        return newError("internal server error" , 500)


def newError(msg , status):
    return Error(msg , status)