# - when there are two classes that need to use each other's features
# - if in the beginning there is only one-way link: add back pointers and change modifiers
#   to update both sets
# - over time, one may find that a client of the referred class also needs to get to the
#   objects that refer to it: requires a backward pointer
# - need to decide which class take charge of the association

# example: a customer can have many orders, while an order belongs to one customer
# if the order is the owning class that manipulates the customer collection, then
# one-way link is sufficient
# but if the customer collection needs access its owning order object, then a bidirectional
# link is required

class Customer(object):
    # the customer class has a reference to a set of orders
    # in the beginning, the class has one-way link to a set of objects of another class

    def __init__(self, name):
        self._name = name
        self._orders = set() # one-way link to a set of objects

    def getOrders(self):
        return self._orders

    def getName(self):
        return self._name

    def addOrder(self, order):
        # if unidirectional association, simply adds the object to the referred class
        # but now it's bidirectional, so the referred class takes charge of the association
        # therefore, needs to call the controlling method of the referred class
        order.setCustomer(self)

class Order(object):
    # the order class has a backward reference to one customer
    # because each order references to only one customer, make the order class take
    # charge of the association
    # every order object belongs to one customer

    def __init__(self, name):
        self._name = name
        self._customer = None # a backward pointer to the referring class, without this it's
                              # simple unidirectional association

    def getCustomer(self):
        return self._customer

    def getName(self):
        return self._name

    def setCustomer(self, customer):
        # the controlling method: takes charge of the association
        self._customer = customer
        self._customer.getOrders().add(self) # needs to update the customer class

john = Customer('John')
order = Order('Pizza')
order.setCustomer(john) # the order class controlls the association
order2 = Order('Burger')
john.addOrder(order2) # the customer class's method also relies on the order class

print 'Customer: %s' % john.getName()
for item in john.getOrders():
    print 'Order: %s' % item.getName()
