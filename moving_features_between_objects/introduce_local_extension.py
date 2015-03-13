# - if a server class needs several additional methods, but you can't modify the class, ex. it
#   is a library class, then create a new class containing the extra methods and make this
#   extension class a subclass or a wrapper of the server class
# - local extension(subclassing or wrapping): all the extension of the original class are
#   put together in the same place; if you introduce foreign methods in many different classes
#   it is hard to maintain and understand the code
# - subclass is prefered as it needs less work, but subclass needs to apply at object-creation time
#   and can't change at run time
# - but use subclass you create a new object of that subclass: make sure that the original object
#   is immutable

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
# 1. local extension: use subclassing
class MyDate(Date):
    # usually we don't override methods in subclass to avoid confusion, but just add new methods

    def getNextDay(self):
        # an added method
        return '%s/%s/%s' % (self.getYear(), self.getMonth(), self.getDate()+1)

mydate = MyDate(2015, 4, 1)
print mydate.getNextDay()

# 2. local extension: use wrapping(delegation)
class MyDate(object):
    # a wrapper class: should preserve all the original methods using delegation and add new
    # behaviors by adding new methods

    def __init__(self, date):
        self._date = date

    def getYear(self):
        # a delegating method
        return self._date.getYear()

    def getMonth(self):
        # a delegating method
        return self._date.getMonth()

    def getDate(self):
        # a delegating method
        return self._date.getDate()

    def getNextDay(self):
        # an added method
        return '%s/%s/%s' % (self.getYear(), self.getMonth(), self.getDate()+1)

mydate = MyDate(Date(2014, 4, 1))
print mydate.getNextDay()

# 3. introduce foreign method
def getNextDay(date):
    # a foreign method with the original object passed in as the first parameter
    return '%s/%s/%s' % (date.getYear(), date.getMonth(), date.getDate()+1)

print getNextDay(Date(2014, 4, 1))


