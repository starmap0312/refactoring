# - if the temp variables are too tangled to replace, use replace method with method object
#   create a new class for the job
# - turn a method into its own object, so that the temp variables become fields of the object
#   the decomposition of the method will become easiler
#
# before: hard to decompose the method
def delta():
    return 100

def gamma(inputValue, quantity, yearToDate):
    # not easy to decompose this method, as there are many tangled temp variables
    value1 = (inputValue * quantity) + delta() # a temp variable
    value2 = (inputValue * yearToDate) + 100 # a temp variable
    if yearToDate - value1 > 100:
        value2 -= 20
    value3 = value2 * 7 # a temp variable
    return value3 - 2 * value1

print gamma(5, 10, 20)

# after: easier to decompose the method
class Gamma(object):

    def __init__(self, inputValue, quantity, yearToDate):
        self.inputValue = inputValue
        self.quantity = quantity
        self.yearToDate = yearToDate
        self.value1 = None # temp variable now becomes object field
        self.value2 = None # temp variable now becomes object field
        self.value3 = None # temp variable now becomes object field

    def compute(self):
        # now easier to decompose this method
        self.value1 = (self.inputValue * self.quantity) + delta()
        self.value2 = (self.inputValue * self.yearToDate) + 100
        if self.yearToDate - self.value1 > 100: # try to extract this part
            self.value2 -= 20                   # try to extract this part
        self.value3 = self.value2 * 7
        return self.value3 - 2 * self.value1

    def new_compute(self):
        # apply extract method
        self.value1 = (self.inputValue * self.quantity) + delta()
        self.value2 = (self.inputValue * self.yearToDate) + 100
        self.extracted_method() # part of the method are extracted into a new method
        self.value3 = self.value2 * 7
        return self.value3 - 2 * self.value1

    def extracted_method(self):
        # as the temp varialbes are now fields, you can use them in any method of the class object
        if self.yearToDate - self.value1 > 100:
            self.value2 -= 20

def newGamma(inputValue, quantity, yearToDate):
    # delegate to the method object
    return Gamma(inputValue, quantity, yearToDate).new_compute()

print newGamma(5, 10, 20)
