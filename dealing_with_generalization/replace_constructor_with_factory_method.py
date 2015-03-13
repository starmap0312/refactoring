# - if you want to do more than "simple construction" when creating an object, then
#   replace the constructor with a factory method

# example
class Employee(object):

    (ENGINEER, SALESMAN, MANAGER) = (0, 1, 2)

    def __init__(self, type):
        self._type = type

    @staticmethod
    def create(type):
        # a factory method
        return Employee(type)

# client code uses factory method
employee = Employee.create(Employee.MANAGER)
print employee._type

# further example: when the type codes are replaced with subclasses
# use factory method can separate the client from the class of object created (i.e. subclasses)

class NewEmployee(object):

    (ENGINEER, SALESMAN, MANAGER) = (0, 1, 2)

    @staticmethod
    def create(type):
        # a switch case here, if add new type code subclass, need to modify here as well
        # if the subclasses do not change, you can create an explict factory method for 
        # each subclasses
        if type == NewEmployee.ENGINEER:
            return Engineer()
        elif type == NewEmployee.SALESMAN:
            return Salesman()
        elif type == NewEmployee.MANAGER:
            return Manager()
        else:
            raise Exception('Incorrect type code')

class Engineer(NewEmployee):

    def __init__(self):
        self._type = NewEmployee.ENGINEER

class Salesman(NewEmployee):

    def __init__(self):
        self._type = NewEmployee.SALESMAN

class Manager(NewEmployee):

    def __init__(self):
        self._type = NewEmployee.MANAGER

# client code: hide the subclasses from the client
employee = NewEmployee.create(NewEmployee.MANAGER)
print employee._type
