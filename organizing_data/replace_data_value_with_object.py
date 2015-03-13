# - OO allows defining new types and turning dumb data into articulate objects
# - in a class, one often uses simple data items, but then realize that objects would be more useful
#   ex: represents phone number as string first, but later requires behavior like formatting,
#       extracting area code, and conversion, etc.
#   if there are only one or two data items, one can write methods in the owning class, but
#   if the codes begins to smell, turn the data items into objects

class Order(object):
    # use simple data type, i.e. string

    def __init__(self, customerName):
        # starts with a data item
        self._customer = customerName

    def getCustomerName(self):
        return self._customer

    def setCustomerName(self, customerName):
        self._customer = customerName

class Customer(object):
    # later, realizes that simple data type (string) is not sufficient, and thus defines an object
    # can define more manipulating methods of the object

    def __init__(self, name):
        self._name = name

    def getName(self):
        return self._name


class NewOrder(object):
    # use a value object: as a rule, value object should be immutable
    # each order has its own Customer object (value object), can further refactor to
    # a reference object, so that all orders for the same customer share the same customer object

    def __init__(self, customerName):
        # takes customerName(string), but can also change to take an existing Customer object
        self._customer = Customer(customerName)

    def getCustomerName(self):
        return self._customer.getName()

    def setCustomer(self, customerName):
        self._customer = Customer(customerName)

# Change Value to Reference
# - when realizes that Customer objects are instances that will be used in many parts of
#   the program, then make them into reference objects

class NewCustomer(object):

    # a static field providing access to all customer objects
    # can also define a new type object
    _instances = dict()

    def __init__(self, name):
        # assuming private, i.e. assuming only create method can construct object
        self._name = name

    def getName(self):
        return self._name

    @staticmethod
    def create(name):
        if name in NewCustomer._instances:
            return NewCustomer._instances[name]

    @staticmethod
    def loadCustomers():
        NewCustomer._instances['Alice'] = NewCustomer('Alice')
        NewCustomer._instances['Bob'] = NewCustomer('Bob')

class ReferenceOrder(object):
    # turn value object into reference object

    def __init__(self, customerName):
        self._customer = NewCustomer.create(customerName)

    def getCustomerName(self):
        return self._customer.getName()

NewCustomer.loadCustomers()
a = ReferenceOrder('Alice')
print a.getCustomerName()
b = ReferenceOrder('Bob')
print b.getCustomerName()
