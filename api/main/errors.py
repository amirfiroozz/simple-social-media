
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


def newError(msg , status):
    return Error(msg , status)