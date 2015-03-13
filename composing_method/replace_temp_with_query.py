# - if a temp variable holds the result of an expression, extract the expression into a method
# - because temp variables are temporary and local, they can only be seen in the context of
#   the method the are used. temp variables tend to encourage longer method
# - by replacing temp with a query method, any method in the class can get at the information,
#   which makes code cleaner
#   moreover, temp variables make extract method difficult, so replace temp with query reduces
#   the number of temp variables, making extract method easier
# - the easy case: the temp is assigned once and the expression has no side effect
#   then extract the expression of the temp into a query method is straightforward
#   but in other cases, you may need to split temporary variable or separate query from modifier
#   first to make the refactoring easier
# - if the temp holds more than an expression, ex. is used to collect result (like summing over
#   a loop), you need to copy some logic into the query method
#   if the loop sum up multiple values, duplicate the loop for each temp, and extract each into
#   a separate query method to make the code easier to understand
# - the performance usually is not the issue, better refactored codes make you optimize the
#   performance in other places

# before
class Price(object):

    def __init__(self, quantity, itemPrice):
        self._quantity = quantity
        self._itemPrice = itemPrice

    def getDiscount(self):
        # the intention of the method is not clear, it contains many logics
        # it's hard to extract method, as the temp appears at many places
        # so we first replace the temp with query
        basePrice = self._quantity * self._itemPrice # a temp variable holding result of expression
        if basePrice > 1000:
            return basePrice * 0.95
        else:
            return basePrice * 0.98

price = Price(50, 30)
print price.getDiscount()

# after: extract the expression into a method
class NewPrice(object):

    def __init__(self, quantity, itemPrice):
        self._quantity = quantity
        self._itemPrice = itemPrice

    def getDiscount(self):
        # method becomes shorter, as the expression is extracted
        # after replace temp with query, we can now further extract the temp discountFactor
        if self.basePrice() > 1000: # can extract this if-else part as the query can be used
                                    # by other method of the class
            discountFactor = 0.95 # another temp varaible
        else:
            discountFactor = 0.98
        return self.basePrice() * discountFactor 

    def basePrice(self):
        # replace temp with query method
        return self._quantity * self._itemPrice

newprice = NewPrice(50, 30)
print newprice.getDiscount()

# further refactored
class NewNewPrice(object):

    def __init__(self, quantity, itemPrice):
        self._quantity = quantity
        self._itemPrice = itemPrice

    def basePrice(self):
        # replace temp with query method
        return self._quantity * self._itemPrice

    def discountFactor(self):
        if self.basePrice() > 1000: # use the basePrice query
            return 0.95
        else:
            return 0.98

    def getDiscount(self):
        # the intention of the method becomes very clear
        return self.basePrice() * self.discountFactor()

newnewprice = NewNewPrice(50, 30)
print newnewprice.getDiscount()
