# - if there are delegations for the entire interface
#   if a subclass use all methods of superclass and follow superclass interface
#     replace the delegating class with a subclass of the delegate
# - delegation
#     client -> wrapper -> delegate    (client is decoupled from the delegate)
#     advantage: easy to compose 
#     disadvantage: extra complexity, creating delegating methods 
# - inheritance
#     client -> subclass -> superclass (client is coupled to subclass)
#     advantage: reduced complexity, easy to extend by subclassing
#     drawback: creates coupling between subclasses
# - replace inheritance with delegation
#   when a class (client) needs to use another class (delegate) but wants more control over its interface
#   expose a set of routines in the wrapper that will provide a cohesive abstraction of the delegate
# - replace delegation with inheritance
#   when a class exposes every public routine of a delegate class, inherit from the delegate class instead of just using the class

# (before: use delegation)
class Person(object):
    # the delegate

    def __init__(self, name):
        self._name = name

    def getName(self):
        return self._name

class Employee(object):
    # a wrapper class (decorator)

    def __init__(self, name, title):
        self._person = Person(name) # the delegate object
        self._title = title

    def getName(self):              # a delegating method
        return self._person.getName()

    def getTitle(self):             # an additional method
        return self._title

# client
employee = Employee('John', 'Senior Engineer')
print employee.getName(), employee.getTitle()

# if wrapper class behaves similarly to the delegate class , use inheritance instead
# (after: replace delegation with inheritance)
class Employee(Person):
    # a subclass: easier to extend

    def setTitle(self, title):
        self._title = title

    def getTitle(self):
        return self._title

# advantage: no need to chase all the delegation
# disadvantage: you cannot switch to other delegate object at run time

# client
employee = Employee()
employee.setName('John')
employee.setTitle('Senior Engineer')
print employee.getName(), employee.getTitle()
