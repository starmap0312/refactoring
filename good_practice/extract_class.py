# I) extract superclass + inheritance
#   1) classes share common behavior as well as implemenation/code
#   2) classes are of natural inheritance relationships
#   3) when all superclass' methods are used (otherwise, use extract class + delegation for better cohesion)
#   advantage: code reuse
#   disadvantage: subclasses are coupled due to inheirtance of a common superclass
# II) extract interface
#   1) classes share common behavior but with different implemenation/code
#   2) when two classes have part of their interfaces in common, extract the subset into an interface
#   advantanges:
#     code gains documentability
#     more extensible: responsibilities are better divided and easier to use and extend 
#   disadvantage: extra complexity
# III) extract class + delegation
#   1) when subclass uses only part of superclass interface
#      i.e. you can make only partial use of the delegated class instead
#   2) classes are not of natural inheritance relationship
#      ex. when subclasses do not want to inherit data/features
#      ex. when some of superclass operations do not make sense for sublcass
#   advantage: code cohesion
#   disadvantage: extra complexity, i.e. extra delegating methods 

# example: I) extract superclass + inheritance
# (before: two irrelevant classes share the common behaviors)
class Employee(object):

    def __init__(self, name, annualCost):
        self._name = name    # common feature
        self._annualCost = annualCost

    def getName(self):       # common behavior
        return self._name

    def getAnnualCost(self): # common behavior with different implementation
        return self._annualCost

class Department(object):

    def __init__(self, name, employees):
        self._name = name    # common feature
        self._staff = employees

    def getStaff(self):
        return self._staff

    def getName(self):       # common behavior
        return self._name

    def getAnnualCost(self): # common behavior with different implementation
        result = 0
        for employee in self.getStaff():
            result += employee.getAnnualCost()
        return result

john = Employee('John', 100000)
tom = Employee('Tom', 200000)
print john.getName(), john.getAnnualCost()
print tom.getName(), tom.getAnnualCost()
cs = Department('CS', [john, tom])
print cs.getName(), cs.getAnnualCost()

# (after: extract superclass + inheritance)
class Party(object):
    # superclass: common features & implementations 

    def __init__(self, name):
        self._name = name          # common feature

    def getName(self):             # common behavior
        return self._name

    def getAnnualCost(self):       # common behavior with different implementation
        raise NotImplementedError

class Employee(Party):
    # subclass

    def __init__(self, name, annualCost):
        super(Employee, self).__init__(name)
        self._annualCost = annualCost # different feature

    def getAnnualCost(self):          # common behavior with different implementation
        return self._annualCost

class Department(Party):
    # wrapper class

    def __init__(self, name, employees):
        super(Department, self).__init__(name)
        self._staff = employees

    def getStaff(self):
        return self._staff

    def getAnnualCost(self):       # common behavior with different implementation
        result = 0
        for employee in self.getStaff():
            result += employee.getAnnualCost()
        return result

john = Employee('John', 100000)
tom = Employee('Tom', 200000)
print john.getName(), john.getAnnualCost()
print tom.getName(), tom.getAnnualCost()
cs = Department('CS', [john, tom])
print cs.getName(), cs.getAnnualCost()


# example: II) extract interface
# (before: class without interface)
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
print employee.getRate()

# (after: create interface for the class)
class Billable(object):
    # interface

    def getRate(self):
        raise NotImplementedError

    def hasSkill(self):
        raise NotImplementedError

class Employee(Billable):
    # implementation 

    def __init__(self, rate, has_skill):
        self._rate = rate
        self._has_skill = has_skill

    def getRate(self):
        return self._rate

    def hasSpecialSkill(self):
        return self._has_skill

employee = Employee(2.5, True)
print employee.getRate()

# example: III) extract class + delegation
class Password(object):
    # extracted class

    def __init__(self, keyname, value):
        self._keyname = keyname
        self._value = value

    def keypair(self):
        return '{0}/{1}'.format(self._keyname, self._value)

    class Database(object):
        # wrapper class

        def __init__(self):                               # encapsulation: hide details from client
            self._passwd = Password('dbuser', 'dbpass')   # do not want to inherit data/features

        def keypair(self):                                # a delegating method
            return self._passwd.keypair()

    class Website(object):
        # wrapper class

        def __init__(self):                               # encapsulation: hide details from client
            self._passwd = Password('webuser', 'webpass') # do not want to inherit data/features

        def keypair(self):                                # a delegating method
            return self._passwd.keypair()

# client
print Password.Database().keypair()
print Password.Website().keypair()

# example: III) extract superclass + inheritance (explict subclasses) 
class Password(object):
    # superclass

    def keypair(self):
        return '{0}/{1}'.format(self._keyname, self._value)

    class Database(Password):
        # explict subclass

        def __init__(self):
            self._keyname = 'dbuser'
            self._value = 'dbpass'

    class Website(Password):
        # explict subclass

        def __init__(self):
            self._keyname = 'webuser'
            self._value = 'webpass'

# client
print Password.Database().keypair()
print Password.Website().keypair()
