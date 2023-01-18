from .models import User
from bson import ObjectId


class UserServices:
    def getAllUsers(self):
        return User.objects.all()

    def getUser(self , userId):
        return User.objects.filter(_id=ObjectId(userId)).first()
    
    def getUserByUsername(self , username):
        return User.objects.filter(username=username).first()

    def newUser(self , username):
        return self.addUser(User(username = username))

    def addUser(self,user):
        user.save()
        return user

    def toDict(self , user:User):
        return {
            "_id":str(user._id),
            "username":user.username,
        }
    
    def toListOfDict(self , users):
        return [self.toDict(user) for user in users]

