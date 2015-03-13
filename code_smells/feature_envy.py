# - object-oriented: a technique to package data with the operations used on that data
# - feature envy: when the method of a class relies very mucn on another class's fields
#   for example, inside the method it invokes half-a-dozen getting methods of another class
#   obviously, the method wants to be elsewhere, so you need to use move method to get it there
#   if only part of the method suffers from feature envy, then you first use extract method
#   to pull that part out and then use move method to get that part to the right place
# - solution to feature envy: "move method" or "extract method + move method"
# - in reality, a method may use features of several classes, so we should move method to 
#   the class that has most of the data(this may require to use extract method first, so that
#   what part goes to which class becomes clearer)
# - rule of thumb: put things together that change together
# - often, data and the operations on it change together, but there are exceptions. when
#   the exceptions occur, we move the behavior to keep changes in one place, ex: strategy pattern
#   and visitor pattern(isolate the changing behaviors, at the cost of further indirection)
