# - inline class: the reverse of extract class
# - if a class isn't doing very much(i.e. a lazy class), move all its features into another class 
#   and then delete it
# - used to resolve shotgun surgery: when a change needs to alter many classes

# before
class Person(object):

    def __init__(self, name):
        self._name = name
        self._phone = Phone()

    def getName(self):
        return self._name

    def getPhoneNumber(self):
        return self._phone.getNumber()

    def getPhone(self):
        return self._phone

class Phone(object):

    def getNumber(self):
        return '(%s) %s' % (self._areaCode, self._number)

    def setAreaCode(self, areaCode):
        self._areaCode = areaCode

    def setNumber(self, number):
        self._number = number

# client
martin = Person('Martin')
phone = martin.getPhone()
phone.setAreaCode('781')
phone.setNumber('191377')
print martin.getPhoneNumber()

# after
class NewPerson(object):
    # move all the features of class Phone into this class, then delete class Phone

    def __init__(self, name):
        self._name = name
        self._areaCode = None # class Phone's field is moved here
        self._number = None # class Phone's field is moved here

    def getName(self):
        return self._name

    def getPhoneNumber(self):
        return '(%s) %s' % (self._areaCode, self._number)

    def setAreaCode(self, areaCode):
        # class Phone's method is moved here
        self._areaCode = areaCode

    def setNumber(self, number):
        # class Phone's method is moved here
        self._number = number

# client
martin = NewPerson('Martin')
martin.setAreaCode('781')
martin.setNumber('191377')
print martin.getPhoneNumber()
