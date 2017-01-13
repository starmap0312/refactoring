# - why/when use interface
#   1) when describing (or exposing) outbound interface of a class, i.e. the operations(or behaviors) a class support
#   2) when a class has many distinct roles in different situations use extract interface for each role
# - advantanges
#   1) makes the code gains documentability
#   2) worthwhile if several classes also want to use the interface
# - when two classes have part of their interfaces in common, or when several clients
#   use the same subset of a class's interface, you can extract the subset into an interface
# - use of a class often means:
#   1) uses all its responsibilities
#   2) use a subset of its responsibilities
#   3) use it to work with another class to handle some requests
#   for 2) and 3), you can extract the subset of responsibilities into an interface, so that the responsibilities are
#   better divided and easier to use if new classes are needed to support the subset
# - extract class vs. extract superclass vs. extract interface
#   extract class: too many duplicate code, puts behavior into a component and then use delegation
#   extract superclass: there is substantial common behavior (or implementation/code)
#   extract interface: bring out common interfaces, not common code (or implementation)

# before: class without interface

class Employee(object):

    def __init__(self, rate, has_skill):
        self._rate = rate
        self._has_skill = has_skill

    def getRate(self):
        return self._rate

    def hasSpecialSkill(self):
        return self._has_skill

def charge(employee, days):
    # a method that wants to charge an employee based on its rate and skill
    base = employee.getRate() * days
    if employee.hasSpecialSkill():
        return base * 1.05 
    return base

employee = Employee(2.5, True)
print charge(employee, 30)

# after: create an interface for the class
class Billable(object):
    # an extracted interface of two methods: getRate() and hasSkill()

    def getRate(self):
        raise NotImplementedError

    def hasSkill(self):
        raise NotImplementedError

class NewEmployee(Billable):
    # the class implements Billable interface, therefore having getRate() and hasSkill() methods

    def __init__(self, rate, has_skill):
        self._rate = rate
        self._has_skill = has_skill

    def getRate(self):
        return self._rate

    def hasSpecialSkill(self):
        return self._has_skill

newemployee = NewEmployee(2.5, True)
print charge(newemployee, 30)
