# - replace type code with state/strategy if have a type code that affects the behavior of 
#   a class but cannot use subclassing
# - used when the type code changes during the life of the object or if another reason prevents
#   subclassing

# before
class Employee(object):

    (ENGINEER, SALESMAN, MANAGER) = (0, 1, 2)

    def __init__(self, type):
        self._type = type

    def payAmount(self):
        # there exist conditional behaviors
        if self._type == Employee.ENGINEER:
            return self._monthlySalary
        elif self._type == Employee.SALESMAN:
            return self._monthlySalary + self._commission
        elif self._type == Employee.MANAGER:
            return self._monthlySalary + self._bonus
        else:
            raise Exception('Incorrect Employee Type')

# if the type code is mutable and one cannot use subclassing
# after
class EmployeeType(object):
    # create a new class for the type code, put type-code related behaviors in subclasses

    (ENGINEER, SALESMAN, MANAGER) = (0, 1, 2)

    def __init__(self):
        self._monthlySalary = 50000
        self._commission = 1000000
        self._bonus = 300000

    def getTypeCode(self):
        return self._code

    @staticmethod
    def create(type):
        if type == EmployeeType.ENGINEER:
            return Engineer()
        elif type == EmployeeType.SALESMAN:
            return Salesman()
        elif type == EmployeeType.MANAGER:
            return Manager()
        else:
            raise Exception('Incorrect Employee Type')

class Engineer(EmployeeType):
    # subclass the type-code class, allowing different behaviors for different type-code subclasses

    def __init__(self):
        super(Engineer, self).__init__()
        self._code = EmployeeType.ENGINEER

    def payAmount(self):
        return self._monthlySalary

class Salesman(EmployeeType):

    def __init__(self):
        super(Salesman, self).__init__()
        self._code = EmployeeType.SALESMAN

    def payAmount(self):
        return self._monthlySalary + self._commission

class Manager(EmployeeType):

    def __init__(self):
        super(Manager, self).__init__()
        self._code = EmployeeType.MANAGER

    def payAmount(self):
        return self._monthlySalary + self._bonus

class NewEmployee(object):
    # the client class HAS_A type-code object, therefore it can change to other type-code 
    # subclass objects at run-time
    # a combination of replace-type-code-with-class and replace-type-code-with-subclass
    (ENGINEER, SALESMAN, MANAGER) = (Engineer(), Salesman(), Manager())

    def getType(self):
        return self._type

    def setType(self, type):
        # able to change to other type-code subclass object at run-time
        self._type = type

    def getTypeCode(self):
        return self._type.getTypeCode()

    def payAmount(self):
        return self._type.payAmount()

employee = NewEmployee() # client object
employee.setType(NewEmployee.ENGINEER) # set its type-code subclass object
print employee.getTypeCode(), employee.payAmount()
employee.setType(NewEmployee.MANAGER) # change to other type-code subclass object at run-time
print employee.getTypeCode(), employee.payAmount()
