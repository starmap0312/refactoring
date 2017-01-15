# - turn the procedural code into object-oriented code
# - when you have code written in a procedural style
#   turn the data records into objects (data class)
#   break up the behavior
#   move the behavior into the object (move method)
# - typical situation
#   1) long procedural methods on a class with little data
#   2) dumb data objects with nothing more than accessors
# - it is OK to have objects with little or no data, but that usually happens in strategy objects
#   with which we can vary behaviors

# before: procedural code with procedures that operate on the data records
def getPrice(order):
    # calculate the price of the order
    pass

def getTaxes(order):
    # calculate the taxes of the order
    pass

# after: object-oriented code
class Order(object):
    # starts with a data class and then move methods in

    def __init__(self, order):
        # first make a data class for data records
        self._order = order

    def getPrice(self):
        # then move behavior on the data records into the data class
        pass

    def getTaxes(self):
        # then move behavior on the data records into the data class
        pass
