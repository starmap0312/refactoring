# - a temp is assigned to once with simple expression and is getting in the way of other 
#   refactoring, then replace all references to the temp with the expression

# before
basePrice = anOrder.basePrice()
return basePrice > 1000

# after: the temp is removed, easier to refactor now
return anOrder.basePrice() > 1000
