# - when you have one class that is doing work that should be done by two, you can create a new 
#   class and move the relevant fields and methods from the old class into the new class
#   and then you use delegation in the old class's method
# - if a class grow too big, containing too many responsibilities, then it is hard to understand
#   the code; or if subsets of data usually change together or dependent on each other, then
#   extract them into a new class

# before
class Person(object):

    def __init__(self, name):
        self._name = name
        self._areaCode = None
        self._number = None

    def getName(self):
        return self._name

    def setAreaCode(self, areaCode):
        self._areaCode = areaCode

    def getAreaCode(self):
        return self._areaCode

    def setNumber(self, number):
        self._number = number

    def getNumber(self):
        return self._number

    def getPhoneNumber(self):
        return '(%s)%s' % (self._areaCode, self._number)

john = Person('John')
john.setAreaCode('04')
john.setNumber('7358992')
print john.getName(), john.getPhoneNumber()

# after
class PhoneNumber(object):
    # the relevant fields and methods are extracted into this new class
    # bundle related variables: areaCode and number

    def setAreaCode(self, areaCode):
        self._areaCode = areaCode

    def getAreaCode(self):
        return self._areaCode

    def setNumber(self, number):
        self._number = number

    def getNumber(self):
        return self._number

    def getPhoneNumber(self):
        return '(%s)%s' % (self._areaCode, self._number)

class NewPerson(object):

    def __init__(self, name):
        self._name = name
        self._phone = PhoneNumber()

    def getName(self):
        return self._name

    def getPhoneNumber(self):
        # use delegation to the new class's method
        return self._phone.getPhoneNumber()

    def getPhone(self):
        # expose phone directly to the client, so the client may change the phone object
        return self._phone

john = NewPerson('John')
phone = john.getPhone()
phone.setAreaCode('04')
phone.setNumber('7358992')
print john.getName(), john.getPhoneNumber()
