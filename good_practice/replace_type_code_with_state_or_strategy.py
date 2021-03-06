# if type code that affects class behavior
#   replace type code with state/strategy if there is a reason that prevents subclassing

# (before: use type code)
class Employee(object):
    # client class

    (ENGINEER, SALESMAN, MANAGER) = (0, 1, 2)

    def __init__(self, code):
        self._code = code # type code

    def payAmount(self):  # define different behavior based on the type code
        if self._code == Employee.ENGINEER:
            return self._monthlySalary
        elif self._code == Employee.SALESMAN:
            return self._monthlySalary + self._commission
        elif self._code == Employee.MANAGER:
            return self._monthlySalary + self._bonus
        else:
            raise Exception('Incorrect Employee Type')

# (after: use state/strategy)
class EmployeeType(object):
    # type-code superclass

    (ENGINEER, SALESMAN, MANAGER) = (0, 1, 2) # type code

    def __init__(self):
        self._monthlySalary = 50000
        self._commission = 1000000
        self._bonus = 300000

    def getCode(self):
        return self._code  # define common behavior in superclass

    def payAmount(self):   # define different behaviors in subclasses
        raise NotImplementedError

    # option 1: use parameterized factory method if type-code changes very often
    @staticmethod
    def create(code):      # define static factory method to decouple client from instances of type-code subclasses
        if code == EmployeeType.ENGINEER:
            return Engineer()
        elif code == EmployeeType.SALESMAN:
            return Salesman()
        elif code == EmployeeType.MANAGER:
            return Manager()
        else:
            raise Exception('Incorrect Employee Type')

    # option 2: use explicit method if type-code does not change often (more descriptive, less extensible)
    @staticmethod
    def create_engineer():
        return Engineer()

    @staticmethod
    def create_manager():
        return Manager()

class Engineer(EmployeeType):
    # type-code subclass

    def __init__(self):
        super(Engineer, self).__init__()
        self._code = EmployeeType.ENGINEER

    def payAmount(self):
        return self._monthlySalary

class Salesman(EmployeeType):
    # type-code subclass

    def __init__(self):
        super(Salesman, self).__init__()
        self._code = EmployeeType.SALESMAN

    def payAmount(self):
        return self._monthlySalary + self._commission

class Manager(EmployeeType):
    # type-code subclass

    def __init__(self):
        super(Manager, self).__init__()
        self._code = EmployeeType.MANAGER

    def payAmount(self):
        return self._monthlySalary + self._bonus

class Employee(object):
    # wrapper class HAS_A type-subclass instance (state/strategy)

    def __init__(self, type):
        self._type = type

    def getCode(self):                # a delegating method
        return self._type.getCode()

    def payAmount(self):
        return self._type.payAmount() # a delegating method

# client: replace type code with state/strategy (decouples client from instances of type-code subclasses)
#         decouple client from type-subclass instances 
employee = Employee(EmployeeType.create(EmployeeType.ENGINEER))
print employee.payAmount()
employee = Employee(EmployeeType.create(EmployeeType.MANAGER))
print employee.payAmount()

# client: comparison with replace type code with subclass
#         client are tightly coupled to type-subclass instances
engineer = EmployeeType.create(EmployeeType.ENGINEER)
print engineer.payAmount()
manager = EmployeeType.create(EmployeeType.MANAGER)
print manager.payAmount()

