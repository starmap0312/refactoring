# - if you have repeated checks for a null value, then replace the null value with a null object
# - if one of your conditional cases is a null, use introduce null object

# before
class Customer(object):
    # abstract class

    def getPlan(self):
        raise NotImplementedError

# client has a conditional that handles the null case
if customer is None:
    plan = doSomething()
else:
    plan = customer.getPlan()

# after: add null object in which it performs doSomething(), thus the conditional can be removed
class NullCustomer(Customer):

    def getPlan(self):
        doSomething()

# client uses polymorphism that is able to perform the null case
plan = customer.getPlan()
