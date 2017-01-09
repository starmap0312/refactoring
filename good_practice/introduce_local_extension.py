# - if a class needs additional methods (functionalities), but you can't modify the class (ex. library class)
#   then either extends (subclasses) the class or decorates (wraps) the class
# - when using extension (subclassing), make sure the original object is immutable

# before: client -> server
class Date(object):
    # the server class which is a library class that cannot be modified

    def __init__(self, year, month, date):
        self._year = year
        self._month = month
        self._date = date

    def getYear(self):
        return self._year

    def getMonth(self):
        return self._month

    def getDate(self):
        return self._date

# after: client -> extension class -> server
#
# 1) use extension (subclassing)
class ExtendedDate(Date):
    # don't override methods in superclass to avoid confusion, just add a new method

    def getNextDay(self):
        # add a new functionality (method)
        return '%s/%s/%s' % (self.getYear(), self.getMonth(), self.getDate() + 1)

mydate = ExtendedDate(2015, 4, 1)
print mydate.getNextDay()
# bad design: we program to implementation, not interface
#             ExtendedDate and Date are tightly coupled 

# 2) use decoration (wrapping)
class ExtendedDate(object):
    # preserve all the original methods using delegation, then add a new method

    def __init__(self, date):
        self._date = date

    def getYear(self):
        return self._date.getYear()

    def getMonth(self):
        return self._date.getMonth()

    def getDate(self):
        return self._date.getDate()

    def getNextDay(self):
        # add a new functionality (method)
        return '%s/%s/%s' % (self.getYear(), self.getMonth(), self.getDate() + 1)

mydate = ExtendedDate(Date(2014, 4, 1))
print mydate.getNextDay()
# good design: we program to interface, not implementation
#              ExtendedDate and Date are loosely coupled
# drawback: code duplication and code complexity
