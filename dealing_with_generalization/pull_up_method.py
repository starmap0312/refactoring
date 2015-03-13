# - have two methods with similar behaviors on subclasses. move them to the superclass
# - the two methods may need to be parameterized so that they end up as the same methods
# - if the two methods refer to features that are on subclass, either generalize the referred
#   method as well, or create an abstract method in the superclass

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
class NewCustomer(object):

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
        # create an abstract method in superclass
        raise NotImplementedError

class RegularCustomer(NewCustomer):

    def chargeFor(self):
        return 100

class PreferredCustomer(NewCustomer):

    def chargeFor(self):
        return 200

regular = RegularCustomer()
regular.createBill()
print regular.getBill()
preferred = PreferredCustomer()
preferred.createBill()
print preferred.getBill()

