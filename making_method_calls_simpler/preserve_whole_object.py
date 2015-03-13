# - if you get several values from an object and passing them in a method, consider to pass
#   the whole object instead(this reduces the parameter list size)
# - if the called method needs other value of the object later, you need not to change the
#   parameter list, as you already pass in the whole object
#   moreover, other methods on the object can be used in the method to calculate intermediate
#   results, thus reducing the possibility of duplicated code
# - makes the code more readable
# - downside: add dependency, the called method now depends on the passed-in object(originally,
#   the called method only depends on the passed-in values)
# - a common case: a class method calls an outside method and pass in several of its own values
#   in this case, you preserve the whole object by passing in this/self

# before
temperature = Temperature()
low = temperature.getLow()
high = temperature.getHigh()
plan = Plan()
withinPlan = plan.withinRange(low, high)

# after
temperature = Temperature()
withinPlan = plan.withinRange(temperature)
