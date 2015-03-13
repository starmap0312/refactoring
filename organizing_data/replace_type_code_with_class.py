# - type code: a special value that indicates a type of instance, often shows up as enumerations
#   or implemented as static final integers
# - if the type code are for information and does not alter the behavior of the class, then 
#   use replace type code with class to give you better type checking and a platform for moving
#   behavior later
#   if the type code affects the behavior of a class, then use replace type code by subclass if
#   possible, otherwise use the more complicated (but more flexible) replace type code by state/
#   strategy
# - replace the type code with a class only if the type code is pure data, i.e. it does not
#   cause different behavior inside a switch statement, because Java can only switch on an integer,
#   not an arbitrary class; the switch has to be removed with replace conditional with polymorphism
#   i.e. replace the type code with subclasses, or replace type code with state/strategy
# - if a class has the numeric type code that does not affect its behavior, then replace the
#   type code with a new class
# - numeric type codes, or enumerations, are a common feature of C-based languages
#   with symbolic names, they are quite readable
#   however, the complier type checks using the number not the symbolic name, 
#   any methods that take the type code as argument expect a number, and there's
#   nothing to force the symbolic name to be used, which can reduce the readablity and 
#   be a source of bugs
# - if replace type code with class, the complier can type check on the class, and by providing
#   factory method for the class, one can statically check that only valid instances are
#   created and that those instances are passed on to the correct objects
# - there might be behavior that is better placed in the type code class, i.e. use move method

# before: a class has a type code
class Person(object):
    # the client class has a type code, i.e. self._bloodGroup
    # the type code is included in the client class, thus the behavior related to the type code
    # is mixed with the client class (limitation of extension)

    (O, A, B, AB) = (0, 1, 2, 3)

    def __init__(self, bloodCode):
        self._bloodCode = bloodCode

    def setBloodCode(self, bloodCode):
        # self._bloodGroup can be set to arbitrary constant, not forced to (0, 1, 2, 3)
        self._bloodCode = bloodCode

    def getBloodCode(self):
        return self._bloodCode

person = Person(Person.A)
# person = Person(2) # no type checks
print person.getBloodCode()

# after: create a new class for the type code
class BloodType(object):

    def __init__(self, code):
        self._code = code

    def getCode(self):
        return self._code

class BloodGroup(object):
    # create a new class for the type code, i.e. a new blood group class with instances 
    # containing the type code number, thus can add type-code related behaviors here
    (O, A, B, AB) = (BloodType(0), BloodType(1), BloodType(2), BloodType(3))
    # type codes are fixed, all type-code objects share the same behavior; use subclassing to
    # allow different behaviors in different type-code objects
    _values = [O, A, B, AB]

    @staticmethod
    def create(code):
        # a factory method for constructing type-code objects
        # if arg not in (0, 1, 2, 3), then an exception will be raised
        # therefore, there will be run-time checking within the blood group class
        return BloodGroup._values[code]

class NewPerson(object):
    # replace the code in Person with code that uses the new class, BloodGroup

    def __init__(self, bloodGroup):
        self._bloodGroup = bloodGroup

    def setBloodGroup(self, bloodGroup):
        self._bloodGroup = bloodGroup

    def getBloodGroup(self):
        return self._bloodGroup

    def getBloodType(self):
        return self._bloodGroup.getCode()

newperson = NewPerson(BloodGroup.A)
#newperson = NewPerson(2) # fail, because there are type checks
#print newperson.getBloodGroup().getCode()
print newperson.getBloodType()

bloodGroup = BloodGroup.create(2)
newperson = NewPerson(bloodGroup)
print newperson.getBloodType()

# another example
class EmployeeType(object):
    # a type-code class, can define type-code related behaviors here; all type codes share
    # the same behavior

    def __init__(self, code):
        self._code = code

    def getTypeCode(self):
        return self._code

class Employee(object):
    # the client class

    (ENGINEER, SALESMAN, MANAGER) = (EmployeeType(0), EmployeeType(1), EmployeeType(2))

    def __init__(self, type):
        self._type = type

    def getType(self):
        return self._type

    def setType(self, type):
        self._type = type

employee = Employee(Employee.ENGINEER)
# employee = Employee(2) # type check: not allowing arbitrary integers
print employee.getType().getTypeCode()
