# - if a class has features that are used only in some instances, then create a subclass
#   for that subset of features
# - extract subclass may be used when a class grows too big
# - the alternative is extract class: extract class => delegation, extract subclass => inheritance
#   delegation is more flexible as you can delegate to another class object at run-time

# before
class JobItem(object):
    # if not all variables are used all of the time, ex. self._employee is used only in some
    # instances, then extract the variable into a new subclass

    def __init__(self, unitPrice, totalPrice, employee):
        self._unitPrice = unitPrice
        self._totalPrice = totalPrice
        self._employee = employee

    def getUnitPrice(self):
        return self._unitPrice

    def getTotalPrice(self):
        return self._totalPrice

    def getEmployee(self):
        return self._employee

class Employee(object):

    def __init__(self, rate):
        self._rate = rate

    def getRate(self):
        return self._rate

# client
jobItem = JobItem(1.0, 10.0, Employee(0.8))
print jobItem.getUnitPrice(), jobItem.getTotalPrice(), jobItem.getEmployee().getRate()

# after
class NewJobItem(object):
    # some of the variables are extracted into a new subclass

    def __init__(self, unitPrice, totalPrice):
        self._unitPrice = unitPrice
        self._totalPrice = totalPrice

    def getUnitPrice(self):
        return self._unitPrice

    def getTotalPrice(self):
        return self._totalPrice

class LaborItem(NewJobItem):
    # the extracted subclass which contains the variable self._employee

    def __init__(self, unitPrice, totalPrice, employee):
        super(LaborItem, self).__init__(unitPrice, totalPrice)
        self._employee = employee

    def getUnitPrice(self):
        # you may also override the superclass methods here
        return self._employee.getRate()

    def getEmployee(self):
        return self._employee

# client
laborItem = LaborItem(1.0, 10.0, Employee(0.8))
print laborItem.getUnitPrice(), laborItem.getTotalPrice(), laborItem.getEmployee().getRate()
