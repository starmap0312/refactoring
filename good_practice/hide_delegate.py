# - encapsulation: hide delegate from client
#   client -> wrapper -> delegate
#   decouple client and delegate: client need not to change accordingly when delegate changes
# - replace inheritance with delegation
#   when a class (client) needs to use another class (delegate) but wants more control over its interface
#   expose a set of routines in the wrapper that will provide a cohesive abstraction of the delegate
# - replace delegation with inheritance
#   when a class exposes every public routine of a delegate class, inherit from the delegate class instead of just using the class
#
# before: tight coupling between client and delegate
class Person(object):

    def __init__(self, department):
        self._department = department

    def getDepartment(self):
        return self._department

class Department(object):
    # the delegate class

    def __init__(self, manager):
        self._manager = manager

    def getManager(self):
        return self._manager

# client: the client knows about (depends on) the delegate object, directly calling its method
john = Person(Department('Professor Chao'))
print john.getDepartment().getManager()
# whenever the delegate object is changed, you may need to change this client code
# ex. when renaming the getManger() method, we need to change the client code

# after: hide delegate from the client
class Person(object):

    def __init__(self, department):
        self._department = department

    def getDepartment(self):
        return self._department

    def getManager(self):
        # delegating method
        return self._department.getManager()

# client: knows nothing about the delegate object, using a delegating method instead
john = Person(Department('Professor Chao'))
print john.getManager()
# when the delegate object is changed, you don't need to change this client code
# ex. when renaming the delegate object's method getManager(), we don't need to change the client code
