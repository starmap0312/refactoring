# replace the constructor with a factory method
#   do more than "simple construction" when creating an object  

# example 1: replace type code with class
class Employee(object):
    # type-code class

    (ENGINEER, SALESMAN, MANAGER) = (0, 1, 2)

    def __init__(self, code):
        self._code = code

    def getCode(self):
        return self._code

    @staticmethod
    def create(code):         # a static factory method can do more things, ex. validation 
        return Employee(code)

# client
# (before: use constructor)
employee = Employee(Employee.MANAGER)
print employee.getCode()

# (after: use factory method, i.e. simple factory)
employee = Employee.create(Employee.MANAGER)
print employee.getCode()

# example 2: replace type code with subclass
class Employee(object):

    (ENGINEER, SALESMAN, MANAGER) = (0, 1, 2)

    def getCode(self):
        return self._code

    # option 1: use switch statement if the type code changes often
    @staticmethod
    def create(code):          # a parameterized factory method which can do more things, ex. switch statement
        if code == Employee.ENGINEER:
            return Engineer()
        elif code == Employee.SALESMAN:
            return Salesman()
        elif code == Employee.MANAGER:
            return Manager()
        else:
            raise Exception('Incorrect type code')

    # option 2: use explict factory method if the type code does not change often
    @staticmethod
    def create_engineer():     # an explict factory method
        return Engineer()

    @staticmethod
    def create_salesman():     # an explict factory method
        return Salesman()

    @staticmethod
    def create_manager():      # an explict factory method
        return Manager()

# advantage: factory methods decouples client from the class being created, i.e. type-code subclasses

class Engineer(Employee):
    # type-code subclass

    def __init__(self):
        self._code = Employee.ENGINEER

class Salesman(Employee):
    # type-code subclass

    def __init__(self):
        self._code = Employee.SALESMAN

class Manager(Employee):
    # type-code subclass

    def __init__(self):
        self._code = Employee.MANAGER

# client: hide instances of type-code subclasses from the client
# (before)
employee = Manager()
print employee.getCode()

# (after)
# option 1
employee = Employee.create(Employee.MANAGER)
print employee.getCode()

# option 2
employee = Employee.create_manager()
print employee.getCode()
