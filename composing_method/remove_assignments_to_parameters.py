# - if the code assigns to a parameter, use a temp variable instead
# - the passed in object can be altered, but don't change it to refer to a different object
#   the reason is to prevent confusion and lack of clarity
#   pass-by-value vs. pass-by-reference: because java and python create a new reference, so
#   if the created reference is assgined to another object in the method, the original reference
#   still refers to the original object, causing confusion
# - you can alter the parameter object but avoid assignment to parameter
#   remove assignments to parameters by creating temp variables

# example
# before
def discount(value):
    value -= 2 # the passed in parameter is changed to refer to a different value
    return value

# after: remove assignments to parameters, create temp reference to make code clearer
def newDiscount(value):
    # if the parameter is assigned, create a temp variable to avoid confusion
    # now there is no assignment to the parameter
    result = value # use a temp variable, this makes you more clearer that 
                   # result is another reference, if it's assigned a new object, the original
                   # reference inputVal will not be changed
    result -= 2 # assign to the temp variable
    return result

value = 80
discount(value)    # the before-code is confusing as one may think parameter value is changed
print value
newDiscount(value) # the refactored code newDiscount is more clear
print value
