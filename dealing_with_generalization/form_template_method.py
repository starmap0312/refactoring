# - two methods in two subclasses that perform similar steps in the same order
#   get the steps into methods, separate what's similar and what's different, and
#   pull those with the same signature up
# - eliminate duplicate code(behavior) by bringing similar methods in subclasses in a superclass

class Rental(object):

    def __init__(self, title, charge):
        self.title = title
        self.charge = charge

# before
class Customer(object):
    # a class with two methods of similar code structure

    def __init__(self):
        self.rentals = [Rental('Book1', 10), Rental('Book2', 20), Rental('Book3', 30)]
        self.name = 'John'
        self.totalCharge = 100

    def textStatement(self):
        result = 'Rental record for %s\n' % self.name
        for item in self.rentals:
            result += '\t%s\t%s\n' % (item.title, item.charge)
        result += 'The total charge is %s' % self.totalCharge
        return result

    def htmlStatement(self):
        result = '<H1>Rental record for %s</H1>\n' % self.name
        for item in self.rentals:
            result += '<BR>%s<BR>%s\n' % (item.title, item.charge)
        result += '<P>The total charge is %s</P>' % self.totalCharge
        return result

customer = Customer()
print customer.textStatement()
print customer.htmlStatement()

# after: extract class, form template method, and use delegation
class Statement(object):
    # extracted class, different format methods are implemented in subclasses

    def headerString(self, customer):
        # different implementation in subclass
        raise NotImplementedError

    def rentalString(self, item):
        # different implementation in subclass
        raise NotImplementedError

    def footerString(self, customer):
        # different implementation in subclass
        raise NotImplementedError

    def value(self, customer):
        # template method: the skeleton of the method(same code structure)
        result = self.headerString(customer)
        for item in customer.rentals:
            result += self.rentalString(item)
        result += self.footerString(customer)
        return result

class TextStatement(Statement):
    # generate text format strings

    def headerString(self, customer):
        return 'Rental record for %s\n' % customer.name

    def rentalString(self, item):
        return '\t%s\t%s\n' % (item.title, item.charge)

    def footerString(self, customer):
        return 'The total charge is %s' % customer.totalCharge

class HtmlStatement(Statement):
    # generate html format strings

    def headerString(self, customer):
        return '<H1>Rental record for %s</H1>\n' % customer.name

    def rentalString(self, item):
        return '<BR>%s<BR>%s\n' % (item.title, item.charge)

    def footerString(self, customer):
        return '<P>The total charge is %s</P>' % customer.totalCharge

class NewCustomer(object):
    # the client class that holds data and that has methods using delegation

    def __init__(self):
        self.rentals = [Rental('Book1', 10), Rental('Book2', 20), Rental('Book3', 30)]
        self.name = 'John'
        self.totalCharge = 100

    def textStatement(self):
        return TextStatement().value(self)

    def htmlStatement(self):
        return HtmlStatement().value(self)

customer = NewCustomer()
print customer.textStatement()
print customer.htmlStatement()
