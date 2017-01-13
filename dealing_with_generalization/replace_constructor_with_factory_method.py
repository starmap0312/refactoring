# - if you want to do more than "simple construction" when creating an object, then
#   replace the constructor with a factory method

# example
class Employee(object):

    (ENGINEER, SALESMAN, MANAGER) = (0, 1, 2)

    def __init__(self, code):
        self._code = code

    def getCode(self):
        return self._code

    @staticmethod
    def create(code):
        # a factory method
        return Employee(code)

# client code uses factory method (simple factory)
employee = Employee.create(Employee.MANAGER)
print employee.getCode()

# further example: when the type codes are replaced with subclasses
# use factory method can separate the client from the class of object created (i.e. subclasses)

class Employee(object):

    (ENGINEER, SALESMAN, MANAGER) = (0, 1, 2)

    def getCode(self):
        return self._code

    @staticmethod
    def create(code):
        # a switch case here, if add new type code subclass, need to modify here as well
        # if the subclasses do not change, you can create an explict factory method for 
        # each subclasses
        if code == Employee.ENGINEER:
            return Engineer()
        elif code == Employee.SALESMAN:
            return Salesman()
        elif code == Employee.MANAGER:
            return Manager()
        else:
            raise Exception('Incorrect type code')

class Engineer(Employee):
    # type-code class

    def __init__(self):
        self._code = Employee.ENGINEER

class Salesman(Employee):
    # type-code class

    def __init__(self):
        self._code = Employee.SALESMAN

class Manager(Employee):
    # type-code class

    def __init__(self):
        self._code = Employee.MANAGER

# client code: hide the subclasses from the client
employee = Employee.create(Employee.MANAGER)
print employee.getCode()
