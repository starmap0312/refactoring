# type code: a type of instance, usually represented by enumerations or static final integers
# 1) if type code does not alter class behavior, then replace type code with class 
#    for better type checking and adding behavior later
# 2) if the type code affects class behavior, then replace type code by subclass or by state/strategy
#    different behaviors are placed in the type code class
#    replace switch/conditional statement with polymorphism

# (before: use type code)
class Person(object):

    (O, A, B, AB) = (0, 1, 2, 3)

    def __init__(self, bloodCode):
        self._bloodCode = bloodCode

    def getBloodCode(self):
        return self._bloodCode

person = Person(Person.O)
print person.getBloodCode()
# drawbacks:
# 1) no type checks: ex. person = Person(2)
# 2) the type code is mixed with the client class, thus limiting its extension

# (after: use class)
class BloodType(object):

  def __init__(self, bloodCode):
      self._bloodCode = bloodCode

  def getBloodCode(self):
    return self._bloodCode

  @staticmethod
  def O():
    return BloodType(0)

  @staticmethod
  def A():
    return BloodType(1)

  @staticmethod
  def B():
    return BloodType(2)

  @staticmethod
  def AB():
    return BloodType(0)

# use factory methods in type class
#   statically check that only valid instances are created 

class Person(object):

    def __init__(self, bloodType):
        self._bloodType = bloodType

    def getBloodCode(self):
        return self._bloodType.getBloodCode()

# client
person = Person(BloodType.O())
print person.getBloodCode()
# advantage
# 1) enables type check: ex. person = Person(2), which will raise type exeception in Java 

# another example
class EmployeeType(object):

    def __init__(self, code):
        self._code = code

    def getCode(self):
        return self._code

class Employee(object):

    (ENGINEER, SALESMAN, MANAGER) = (EmployeeType(0), EmployeeType(1), EmployeeType(2))

    def __init__(self, type):
        self._type = type

    def getCode(self):
        return self._type.getCode()

employee = Employee(Employee.ENGINEER)
print employee.getCode()
# advantage
# 1) enables type check: ex. employee = Employee(2), which will raise type exeception in Java 