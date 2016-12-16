# - if a conditional perform different behavior depending on the type code, then move the
#   conditional to an overriding method in a subclass, and make original method abstract
# - the clients do not need to know about the subclasses, which reduces the dependencies in the
#   system(clients depend only on the abstract class), make code easier to update
# - polymorphism: allows you avoid writing an explicit conditional when object's behavior depends
#   on its type
# - advantage of polymorphism: when the same conditions appear in many places, use polymorphism
#   is easier to maintain and extend(ex. update or add a new type)

# before
class Employee(object):
    # use switch statement to perform different behavior for different type codes

    (ENGINEER, SALESMAN) = (0, 1)

    def __init__(self, salary, commission, bonus):
        self._salary = salary
        self._commission = commission
        self._bonus = bonus

    def setType(self, type):
        # the type code is a primitive data type
        self._type = type

    def getSalary(self):
        return self._salary

    def getCommission(self):
        return self._commission

    def getBonus(self):
        return self._bonus

    def payAmount(self): # exhibit different behaviors based on different type codes
        # the switch statement may appear in many places, the type code related behaviors are
        # mixed with the client class here
        if self._type == Employee.ENGINEER:
            return self.getSalary() + self.getCommission()
        elif self._type == Employee.SALESMAN:
            return self.getSalary() + self.getBonus()

employee = Employee(68000, 100000, 200000)
employee.setType(Employee.ENGINEER)
print employee.payAmount()
employee.setType(Employee.SALESMAN)
print employee.payAmount()

# after: replace type code with state/strategy
class Employee(object):
    # the client class of type code objects, using delegation

    (ENGINEER, SALESMAN) = (0, 1)

    def __init__(self, salary, commission, bonus):
        self._salary = salary
        self._commission = commission
        self._bonus = bonus

    def setType(self, type):
        # can set to other type code object(state/strategy) at run-time
        self._type = type

    def getSalary(self):
        return self._salary

    def getCommission(self):
        return self._commission

    def getBonus(self):
        return self._bonus

    def payAmount(self): # exhibit the same behavior by delegating to type classes
        # the switch statement is replaced by delegation to different type code objects
        return self._type.payAmount(self)

class EmployeeType(object):
    # type code has its own class: you can put type code related behaviors/operations here
    # separate type code related responsibilities, make extension easier

    def getTypeCode(self):
        raise NotImplementedError

    def payAmount(self, employee):
        raise NotImplementedError

class Engineer(EmployeeType):
    # one kind of type code object

    def getTypeCode(self):
        return Employee.ENGINEER

    def payAmount(self, employee):
        return employee.getSalary() + employee.getCommission()

class Salesman(EmployeeType):
    # one kind of type code object

    def getTypeCode(self):
        return Employee.SALESMAN

    def payAmount(self, employee):
        return employee.getSalary() + employee.getBonus()

employee = Employee(68000, 100000, 200000)
employee.setType(Engineer())
print employee.payAmount()
employee.setType(Salesman())
print employee.payAmount()

