# - simplify an overly-complex class by turning it into a group of subclasses
# - when you have a class that is doing too much work, ex. through many conditional statements,
#   then create a hierarchy of classes in which each subclass represents a special case
# - it is common to design a class which implements one idea but it evolves to implement
#   several ideas later, ex. the class contains many flags and conditional expressions at the end
#   then you need to separate the cases from each other(if the conditional logic is not static
#   during the life of the object, you need to use extract class first)
# - for easier cases, use replace type code with subclasses, replace type code with state/strategy,
#   or replace conditional with polymorphism

# before
class Customer(object):

    def __init__(self, billingScheme, typeCode):
        self._billingScheme = billingScheme
        self.typeCode = typeCode

class BillingScheme(object):
    # a complex class that contains many conditional logic

    def createBill(self, customer):
        # complex conditional logic: first use decompose conditional to simplify the code first
        if customer.typeCode == 'Bussiness':
            create_bussiness_bill()
        elif customer.typeCode == 'Residential':
            create_residential_bill()
        elif customer.typeCode == 'Disability':
            create_disability_bill()

# after: create a subclass for each variation of BillingScheme
# you may need to repeatedly refactor the code to separate the varying code from the code that 
# stays the same first, using extract method and decompose conditional
class BillingScheme(object):
    # a superclass: use replace constructor with factory method

    def createBill(self, customer):
        # implemented in subclasses
        raise NotImplementedError

    @staticmehod
    def createBillingScheme(typeCode):
        if typeCode == 'Bussiness':
            return BusinessBillingScheme()
        elif typeCode == 'Residential':
            return ResidentialBillingScheme()
        elif typeCode == 'Disability':
            return DisabilityBillingScheme()

class BusinessBillingScheme(BillingScheme):

    def createBill(self, customer):
        create_bussiness_bill()

class ResidentialBillingScheme(BillingScheme):

    def createBill(self, customer):
        create_residential_bill()

class DisabilityBillingScheme(BillingScheme):

    def createBill(self, customer):
        create_disability_bill()

