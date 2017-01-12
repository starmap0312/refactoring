# if type code that affects class behavior: replace type code with state/strategy
#   if there is a reason that prevents subclassing

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
        return self._code         # define common behavior in superclass

    def payAmount(self):
        raise NotImplementedError # define different behaviors in subclasses

    @staticmethod
    def create(code):
        if code == EmployeeType.ENGINEER:
            return Engineer()
        elif code == EmployeeType.SALESMAN:
            return Salesman()
        elif code == EmployeeType.MANAGER:
            return Manager()
        else:
            raise Exception('Incorrect Employee Type')

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
    # client/wrapper class (decorator): HAS_A type-subclass instance (state/strategy)

    def __init__(self, type):
        self._type = type

    def getCode(self):
        return self._type.getCode()

    def payAmount(self):
        return self._type.payAmount()

# client: replace type code with state/strategy
engineer = EmployeeType.create(EmployeeType.ENGINEER)
employee = Employee(engineer)
print employee.payAmount()
manager = EmployeeType.create(EmployeeType.MANAGER)
employee = Employee(manager)
print employee.payAmount()
# advantage: client are decoupled from type-subclass instances
#            when type subclass changes, client code is not affected

# client: comparison with replace type code with subclass
engineer = EmployeeType.create(EmployeeType.ENGINEER)
print engineer.payAmount()
manager = EmployeeType.create(EmployeeType.MANAGER)
print manager.payAmount()
# disadvantage: client are tightly coupled to type-subclass instances
