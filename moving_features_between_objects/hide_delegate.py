# - when a client is calling a method defined on its server's field, which is a delegate object. 
#   the client then needs to know about the delegate object 
#   we can hide the delegate object from the client by creating a method(the delegating method) 
#   on the server which makes the call on the delegate object
#   this way, the client knows nothing about the delegate object(client->server->delegate)
# - the benefit of such encapsulation is that when the delegate object is changed, it does not
#   affect both the client and server class, but only the server class
#   in other words, the dependency of client and delegate is removed, the change does not 
#   propagate to the client, making the code easier to extend
# - well encapsulation: when things change, fewer objects need to be told about the change

# before
class Person(object):
    # the server class

    def setDepartment(self, department):
        self._department = department

    def getDepartment(self):
        return self._department

class Department(object):
    # the delegate class

    def __init__(self, manager):
        self._manager = manager

    def getManager(self):
        return self._manager

# client: as the client knows about the delegate object, it can directly calls its method
john = Person()
john.setDepartment(Department('Professor Chao'))
# the client directly calls the delegate object's method, thus the client code depends on the
# delegate object now
# whenever the delegate object is changed, you may need to change this client code
# ex. if you rename the getManger() method to getManagerName(), you need to change the 
# client code here too
print john.getDepartment().getManager()

# after: hide delegate from the client by creating a delegating method in the server class
class Person(object):
    # the server class

    def setDepartment(self, department):
        self._department = department

    def getDepartment(self):
        return self._department

    def getManager(self):
        # the delegating method
        return self._department.getManager()

# the client does not directly call the delegate object's method but through the delegating method
john = Person()
john.setDepartment(Department('Professor Chao'))
# the client does not call the delegate object's method and knows nothing about the delegate object
# therefore, when the delegate object is changed, you don't need to change this client code
# instead, changing the server class's delegating method is sufficient
# ex. if you rename the delegate object's method getManager() to getManagerName(), you don't need
# to change this client code here
print john.getManager()
