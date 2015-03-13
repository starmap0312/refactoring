# - if there are delegations for the entire interface, then make the delegating class a
#   subclass of the delegate
# - a subclass should use all the methods of superclass and follow the interface of the
#   superclass
# - client -> server -> delegate: this is used when you create too many delegating methods 
#   at the server class, and later figure out that making the server class a subclass of the
#   the delegate class is a better choice

# before
class Person(object):

    def setName(self, name):
        self._name = name

    def getName(self):
        return self._name

class Employee(object):

    def __init__(self):
        self._person = Person() # the delegate object

    def setName(self, name):
        # a delegating method
        self._person.setName(name)

    def getName(self):
        # a delegating method
        return self._person.getName()

    def setTitle(self, title):
        self._title = title

    def getTitle(self):
        return self._title

# client
employee = Employee()
employee.setName('John')
employee.setTitle('Senior Engineer')
print employee.getName(), employee.getTitle()

# after: as the server class behaves similarly to the delegate class , we use inheritance instead
class Employee(Person):
    # the server class is a subclass of the delegate class, so it becomes easier to extend
    # the behaviors without chasing all the delegation, but the limitation is that you cannot
    # switch to other delegate object at run time

    def setTitle(self, title):
        self._title = title

    def getTitle(self):
        return self._title

# client
employee = Employee()
employee.setName('John')
employee.setTitle('Senior Engineer')
print employee.getName(), employee.getTitle()
