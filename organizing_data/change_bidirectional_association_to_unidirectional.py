# - when you have a two-way association but one class no longer needs features from the other,
#   then drop the unneeded end of the association(this reduces the intimacy of the two classes)
# - bidirectional associations are useful, but they carry a price: the added complexity of
#   maintaining the two-way links(the interdependeny: a change of either one affects the other)
# - two-way links could be a source of errors: can lead to zombies(an object still hangs around
#   because of a reference not cleared)
# - if the two classes are in two separate packages, you get an interdependency betwenn two
#   packages(a change to one package may cause a change to the other)
# - highly coupled system: a little change leads to lots of unpredictable results

# before: order <-> customer
class Order(object):
    # the class depends on a Customer object; more specifically, it depends on a Customer object's
    # field _discount in its getPrice() method

    def __init__(self):
        self._customer = None # has a reference to a Customer object

    def getCustomer(self):
        return self._customer

    def setCustomer(self, customer):
        if self._customer is not None:
            self._customer.removeOrder(self)
        self._customer = customer
        self._customer.setOrder(self)

    def getPrice(self):
        # the method needs a field of the Customer object, i.e. _discount
        # see if the method can get the field in another way, for example, through parameter
        return 100.0 * (1 - self._customer.getDiscount())

class Customer(object):
    # the class depends on the Order class, as it keeps a reference to an Order object

    def __init__(self, discount):
        self._order = None # has a reference to an Order object
        self._discount = 0.05

    def setOrder(self, order):
        self._order = order

    def removeOrder(self):
        self._order = None

    def getDiscount(self):
        return self._discount

# client
order = Order()
customer = Customer(discount=0.05)
order.setCustomer(customer)
print order.getPrice()

# after: order <- customer: break the link from order to customer
class Order(object):
    # remove the dependency to the Customer class, i.e. no longer needs to keep a reference
    # to a Customer object

    def getPrice(self, customer):
        # the method gets the Customer object's field by passing in the Customer object as
        # a parameter, thus the Order class no longer needs to keep a reference to the 
        # Customer object
        return 100.0 * (1 - customer.getDiscount())

# client
order = Order()
customer = Customer(discount=0.05)
customer.setOrder(order)
print order.getPrice(customer)
