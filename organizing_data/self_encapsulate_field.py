# - debate: whether an object should access its own data directly or through accesors
#   generally use direct access because it is simple to do refactoring
# - within the class the variable is defined: access the variable freely vs. use accessors
# comparison: direct vs. indirect access
# 1) indirect access
#    allow subclass to overwrite how to get the information
#    support lazy initialization: i.e. initializes the value only when you need to use it
# 2) direct access (bad design)
#    the code is easier to read
# - self encapsulate field: use getting and setting methods
# - use direct access first, and switch to indirect access if necessary
#   ex: when access a field in a superclass, but want to override the variable access with
#   a computed value in the subclass

class DirectIntRange(object):
    # direct access example

    def __init__(self, low, high):
        self._low = low
        self._high = high

    def includes(self, num):
        return num >= self._low and num <= self._high

class IndirectIntRange(object):
    # indirect access example

    def __init__(self, low=None, high=None):
        # do not use setting method in constructor, often assumed that setter is used after
        # the object is constructed
        # it is ok to use direct access in constructor, as initialization of fields
        self._low = low
        self._high = high

    def getLow(self):
        return self._low

    def setLow(self, low):
        self._low = low

    def getHigh(self):
        return self._high

    def setHigh(self, high):
        self._high = high

    def includes(self, num):
        return num >= self.getLow() and num <= self.getHigh()

a = DirectIntRange(1, 4)
print a.includes(3)
print a.includes(5)

b = IndirectIntRange()
b.setLow(1)
b.setHigh(4)
print b.includes(3)
print b.includes(5)

class CappedRange(IndirectIntRange):
    # can override getting method: change the behavior of accessing the field

    def __init__(self, low, high, cap):
        super(CappedRange, self).__init__(low, high)
        self._cap = cap

    def getCap(self):
        return self._cap

    def getHigh(self):
        return min(super(CappedRange, self).getHigh(), self.getCap())

c = CappedRange(1, 4, 3)
print c.getHigh()
