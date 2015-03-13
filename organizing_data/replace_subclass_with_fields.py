# - if subclasses vary only in methods that return constant data, then one can replace subclass
#   with fields
# - eliminate subclasses and make the desgin structure simpler
# - subclasses can have different behaviors or return different values for an accessor, but
#   if a subclass consists only of constant methods and is not doing enough to be worth existing,
#   remove the subclass to reduce the complexity

# before
class Person(object):
    # abstract class

    def isMale(self):
        raise NotImplementedError

    def getCode(self):
        raise NotImplementedError

    @staticmethod
    def createFemale():
        return Female()

    @staticmethod
    def createMale():
        return Male()

class Female(Person):
    # subclass not doing much but returns constant values

    def isMale(self):
        # return cosntant value
        return False

    def getCode(self):
        return 'F'

class Male(Person):

    def isMale(self):
        return True

    def getCode(self):
        return 'M'

female = Person.createFemale()
print female.isMale(), female.getCode()
male = Person.createMale()
print male.isMale(), male.getCode()

# after: reduce the complexity of sublcass
class NewPerson(object):
    # remove subclasses and use fields instead
    # have factory method for creating objects

    def __init__(self, isMale, code):
        self._isMale = isMale
        self._code = code

    def isMale(self):
        return self._isMale

    def getCode(self):
        return self._code

    @staticmethod
    def createFemale():
        return NewPerson(False, 'F')

    @staticmethod
    def createMale():
        return NewPerson(True, 'M')

female = NewPerson.createFemale()
print female.isMale(), female.getCode()
male = NewPerson.createMale()
print male.isMale(), male.getCode()

