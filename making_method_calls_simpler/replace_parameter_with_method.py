# - if a parameter can be obtained by invoking a method, and the receiver function can also
#   invoke the method, then remove the parameter, and let the receiver function invoke the
#   method itself(reduce the parameter list size)
# - methods with short parameter list are easier to understand

# before
class Product(object):

    def __init__(self, quantity, itemPrice):
        self._quantity = quantity
        self._itemPrice = itemPrice

    def getPrice(self):
        basePrice = self._quantity * self._itemPrice # a temp variable used as a parameter
        if self._quantity > 100:
            discountLevel = 2 # a temp variable used as a parameter
        else:
            discountLevel = 1
        # the method depends on two parameters
        finalPrice = self.discountedPrice(basePrice, discountLevel) # a temp variable
        return finalPrice

    def discountedPrice(self, basePrice, discountLevel):
        # the method can get both parameters by itself, so try to remove the parameters
        if discountLevel == 2:
            return basePrice * 0.1
        else:
            return basePrice * 0.05

print Product(80, 100.0).getPrice()

# after
class NewProduct(object):

    def __init__(self, quantity, itemPrice):
        self._quantity = quantity
        self._itemPrice = itemPrice

    def getBasePrice(self):
        # replace parameter with method
        return self._quantity * self._itemPrice

    def getDiscountedLevel(self):
        # replace parameter with method
        return 2 if self._quantity > 100 else 1

    def getPrice(self):
        # both parameters are removed and replaced with methods
        # the method get the parameters by methods instead
        if self.getDiscountedLevel() == 2:
            return self.getBasePrice() * 0.1
        else:
            return self.getBasePrice() * 0.05

print NewProduct(80, 100.0).getPrice()
