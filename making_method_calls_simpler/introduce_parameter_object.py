# - if you have a group of parameters that naturally go together(related), replace them with
#   a parameter object
#   this shortens the parameter list size, making the method call looks simpler
#   if a group of parameters go together very often(several methods/classes use this group),
#   then group these parameters into objects
# - the code will be more consistent because the new object data are manipulated by its accessors
#   (thus easier to understand and modify the code)
# - if later some of the behaviors of manipulating the data can be extracted into the new object
#   class, you have the chance to remove some duplicated codes

# before
class Account(object):

    def __init__(self):
        self._entities = []

    def getFlowBetween(self, start, end):
        # many methods use this pair of parameters, so consider to extract them into a new object
        result = 0
        for element in self._entities:
            if element.getDate() >= start and element.getDate() <= end:
                result += element.getValue()
        return result

# client
account = Account()
flow = account.getFlowBetween(start, end)

# after
class DateRange(object):
    # a new object containing a group of related parameters

    def __init__(self, start, end):
        self._start = start
        self._end = end

    def getStart(self):
        return self._start

    def getEnd(self):
        return self._end

class NewAccount(object):
    # replace a group of parameters with a parameter object

    def __init__(self):
        self._entities = []

    def getFlowBetween(self, dateRange):
        # the parameter list size is shortened
        result = 0
        for element in self._entities:
            if (element.getDate() >= dateRange.getStart() and 
                element.getDate() <= dateRange.getEnd()):
                result += element.getValue()
        return result

# client
account = NewAccount()
flow = account.getFlowBetween(DateRange(start, end))
