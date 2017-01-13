# - if two methods with similar behaviors on subclasses. pull them up to superclass
# - the two methods may need to be parameterized so that they end up as an identical method
# - if the two methods refer to features that are in subclasses
#   1) generalize the referred method as well, or
#   2) create an abstract method in the superclass

# before
class Customer(object):

    def __init__(self):
        self.bill = None

    def addBill(self, amount):
        self.bill = amount

    def getBill(self):
        return self.bill

class RegularCustomer(Customer):

    def createBill(self):
        amount = self.chargeFor() # to be pulled, but it refers to a sublcass method
        self.addBill(amount)

    def chargeFor(self):
        return 100

class PreferredCustomer(Customer):

    def createBill(self):
        amount = self.chargeFor() # to be pulled, but it refers to a subclass method
        self.addBill(amount)

    def chargeFor(self):
        return 200

regular = RegularCustomer()
regular.createBill()
print regular.getBill()
preferred = PreferredCustomer()
preferred.createBill()
print preferred.getBill()

# after
class Customer(object):

    def __init__(self):
        self.bill = None

    def addBill(self, amount):
        self.bill = amount

    def getBill(self):
        return self.bill

    def createBill(self):
        amount = self.chargeFor()
        self.addBill(amount)

    def chargeFor(self):
        raise NotImplementedError # create an abstract method in superclass

class RegularCustomer(Customer):

    def chargeFor(self):
        return 100

class PreferredCustomer(Customer):

    def chargeFor(self):
        return 200

regular = RegularCustomer()
regular.createBill()
print regular.getBill()
preferred = PreferredCustomer()
preferred.createBill()
print preferred.getBill()

