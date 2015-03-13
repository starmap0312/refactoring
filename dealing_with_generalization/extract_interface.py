# - why/when use interface: 1. when a class has many distinct roles in different situations
#   use extract interface for each role
#   2. when you want to describe(or expose) the outbound interface of a class, i.e. the
#   operations(or behaviors) a class support
# - when two classes have part of their interfaces in common, or when several clients
#   use the same subset of a class's interface, you can extract the subset into an interface
# - use of a class often means 1. uses all its responsibilities, or 2. use a subset of its 
#   responsibilities, or 3. use it to work with another class to handle some requests
#   for 2. and 3., you can extract the subset of responsibilities into an interface, so that
#   the responsibilities are better divided and easier to use if new classes are needed to
#   support the subet
# - extract superclass and extract interface are similar in certain ways: extract interface
#   only bring out common interfaces, not common code(or implementation); sometimes you have
#   to choose between extract class, extract superclass, and extract interface
#   if there is substantial common behavior(code), use extract superclass
#   if too many duplicate code, use extract class which puts behavior into a component and then
#   use delegation

# before

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

# after
class Billable(object):
    # an extracted interface of two methods: getRate() and hasSkill()
    # defining the interface makes the code gains documentability, which would be worthwhile
    # if several classes also want to use the interface (ex. Computer class can also be Billable)

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
