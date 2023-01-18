
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
    
    def postNotFoundedError(self):
        return newError("post not founded" , 404)
    
    def userNotFoundedError(self):
        return newError("user not founded" , 404)
    
    def alreayLikedError(self):
        return newError("internal server error" , 409)
    
    def internalError(self):
        return newError("internal server error" , 500)


def newError(msg , status):
    return Error(msg , status)