# - problem
#   two classes have similar methods but different interfaces
# - effect 
#   a kind of duplicated code
# - easy case
#   two classes perform identical functions but have different method names
# - root cause
#   the programmer who created a class probably didn't know that a functionally equivalent class already exists
# - solution
#   rename method, move method, parameterize method to make the signature and implementation identical
#   delete one of the class if only part of the functionality of the classes is duplicated
#   extract superclass and make classes become sublcasses
# - after the refactoring, you get rid of the duplicated code and improve readability
