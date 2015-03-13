# - if a class is doing too much simple delegation, and you get a lot of delegating methods,
#   then get the client to call the delegate object's methods directly
# - advantage of hide delegate(encapsulation): remove dependencies, make extension easier
# - disadvantage of hide delegate(encapsulation): whenever you want to use a new feature of
#   the delegate object, you need to add a simple delegating method at the server class
#   the server class is just a middle man, and perhaps it is better to let the client call
#   the delegate object directly

# before: client -> server -> delegate
class Person(object):
    # the server class

    def __init__(self, department):
        self._department = department

    def getDepartment(self):
        return self._department

    def getManager(self):
        # a delegating method
        return self._department.getManager()

class Department(object):
    # the delegate class

    def __init__(self, manager):
        self._manager = manager

    def getManager(self):
        return self._manager

# client
john = Person(Department('Tom'))
print john.getManager()

# after: client -> server
#               -> delegate
class Person(object):
    # the server class

    def __init__(self, department):
        self._department = department

    def getDepartment(self):
        return self._department

john = Person(Department('Tom'))
print john.getDepartment().getManager() # the client access the delegate object directly
