# - when two classes have similar features
#     extract superclass and move the common features to the superclass(common behaviors/code) 
# - in contrast, if there are no common code (behavior)
#     extract interface
# - often you don't notice the common parts when creating some classes, in which case you need
#   to extract the common parts into a superclass later
# - "extract superclass + inheritance" vs. "extract class + delegation"
# - use "extract superclass + inheritance" if 
#   two classes share same "interface" and "behavior" and you feel that inheritance is a good choice
# - use "extract class + delegation" if
#   1) subclass uses only part of superclass interface, or
#   2) subclass does not want to inherit data
#   3) many of superclass operations do not make sense for sublcass
# - use "extract superclass + inheritance" if you want to use all superclass's methods
#   use "extract class + delegation" if you make partial use of the delegated class (the cost is extra delegating methods)
# - "replace inheritance with delegation" or "replace delegation with inheritance" if
#   make the wrong choice and want to switch to the other option

# before
class Employee(object):

    def __init__(self, name, annualCost):
        self._name = name
        self._annualCost = annualCost

    def getName(self):
        return self._name

    def getAnnualCost(self):
        return self._annualCost

class Department(object):

    def __init__(self, name):
        self._name = name
        self._staff = []

    def addStaff(self, employee):
        self._staff.append(employee)

    def getStaff(self):
        return self._staff

    def getName(self):
        return self._name

    def getAnnualCost(self):
        result = 0
        for employee in self.getStaff():
            result += employee.getAnnualCost()
        return result

john = Employee('John', 100000)
tom = Employee('Tom', 200000)
print john.getName(), john.getAnnualCost()
print tom.getName(), tom.getAnnualCost()
cs = Department('CS')
cs.addStaff(john)
cs.addStaff(tom)
print cs.getName(), cs.getAnnualCost()

# after: extract superclass + inheritance
class Party(object):
    # common interface and behavior are extracted into the superclass, inheritance are
    # then applied

    def __init__(self, name):
        self._name = name

    def getName(self):
        return self._name

    def getAnnualCost(self):
        raise NotImplementedError

class NewEmployee(Party):

    def __init__(self, name, annualCost):
        super(NewEmployee, self).__init__(name)
        self._annualCost = annualCost

    def getAnnualCost(self):
        return self._annualCost

class NewDepartment(Party):

    def __init__(self, name):
        super(NewDepartment, self).__init__(name)
        self._staff = []

    def addStaff(self, employee):
        self._staff.append(employee)

    def getStaff(self):
        return self._staff

    def getAnnualCost(self):
        result = 0
        for employee in self.getStaff():
            result += employee.getAnnualCost()
        return result

john = NewEmployee('John', 100000)
tom = NewEmployee('Tom', 200000)
print john.getName(), john.getAnnualCost()
print tom.getName(), tom.getAnnualCost()
cs = NewDepartment('CS')
cs.addStaff(john)
cs.addStaff(tom)
print cs.getName(), cs.getAnnualCost()
