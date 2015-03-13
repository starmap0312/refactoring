# - complex conditional logic makes the code hard to understand, and tends to lead to long methods
# - if you have a complicated conditional(if-then-else) statement, extract methods from the
#   condition, then-part and else-part
# - after simplifying the conditionals, the intention of the conditionals become clear

# before
SUMMER_START = 'July'
SUMMER_END = 'October'
winter_rate = 1.0
summer_rate = 1.2
service_fee = 150.0

if date.before(SUMMER_START) or date.after(SUMMER_END): # extract method
    charge = quantity * winter_rate + service_fee # extract method
else:
    charge = quantity * winter_rate # extract method

# after: extract methods from the condition, if-part, and else-part
def notSummer(date):
    return date.before(SUMMER_START) or date.after(SUMMER_END)

def winterCharge(quantity):
    return quantity * winter_rate + service_fee

def summerCharge(quantity):
    return quantity * winter_rate

# the intention of the conditional becomes very clear
if notSummer(date):
    charge = winterCharge(quantity)
else:
    charge = summerCharge(quantity)
