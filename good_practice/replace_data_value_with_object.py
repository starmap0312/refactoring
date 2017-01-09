# turn dumb data into articulate objects
#   ex: string vs. phone number (add behavior like formatting)
#       string vs. area code (add behavior like conversion)
#
# (before: use simple data type, ex. string)
class Order(object):

    def __init__(self, customerName):
        self._customer = customerName # name string

    def getCustomerName(self):
        return self._customer

# client
order = Order('John')
print order.getCustomerName()

# (after: use value object, which is immutable)
class Customer(object):

    def __init__(self, name):
        self._name = name

    def getName(self):
        return self._name

class Order(object):

    def __init__(self, customerName):
        self._customer = Customer(customerName)

    def getCustomerName(self):
        return self._customer.getName()

# client
order = Order('John')
print order.getCustomerName()

