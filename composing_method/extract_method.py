# - duplicated code: unify same code structures via extract method, i.e. if have the same 
#   expression in two methods of the same class
# - readability: if a method is too long or the code needs a comment to understand its purpose
# - short, well-named method: increase code re-use, high-level methods that uses a series of
#   short methods is more readable
# - method length is not the issue, the issue is the semantic distance between method name and
#   method body: if extracting improves readability, do it, even when its name is longer than body
# - naming is important: short methods only work if they are well named

# example
class Payment(object):

    def __init__(self, id, name, amount):
        self._id = id
        self._name = name
        self._amount = amount

    def printID(self):
        print self._id

    def printDetails(self):
        self.printID()
        # have a fragment of code that can be grouped together
        print 'name: %s' % self._name
        print 'amount: %s' % self._amount

class NewPayment(object):

    def __init__(self, id, name, amount):
        self._id = id
        self._name = name
        self._amount = amount

    def printID(self):
        print self._id

    def printInfo(self):
        # turn the fragment of code into a method with a name that explains its purpose
        print 'name: %s' % self._name
        print 'amount: %s' % self._amount

    def printDetails(self):
        # improved code readability: knowing better about the method's intention
        self.printID()
        self.printInfo()

payment = Payment('001', 'Bob', '1000')
newpayment = NewPayment('002', 'Alice', '50000')
payment.printDetails()
newpayment.printDetails()

# another example
elements = [10.0, 12.0, 20.0]
name = 'John'

def printOwing():

    # print banner (extract method)
    print '***** Banner ******'

    # calculate outstanding (extract method)
    outstanding = 0.0 # a temp variable
    for e in elements:
        outstanding += e

    # print details (extract method)
    print 'name: %s' % name
    print 'amount: %s' % outstanding

printOwing()

# refactored
def printBanner():
    print '***** Banner ******'

def getOutstanding():
    # move the temp variable, outstanding, into the extracted method, and rename it to result
    # as the temp variable is used after the extracted, return its value
    # if there are more than one value that needs to be returned, the best option is to pick
    # different code to extract (separate them, so only one value is returned in each extracted
    # code)
    result = 0.0
    for e in elements:
        result += e
    return result

def printDetails(outstanding):
    # as outstanding is a temp variable that is read and not assigned, so it is easy to refactor 
    # by passing it as a parameter
    print 'name: %s' % name
    print 'amount: %s' % outstanding

def newPrintOwing():
    # the refactored code becomes easier to read
    printBanner()
    outstanding = getOutstanding()
    printDetails(outstanding)

newPrintOwing()
