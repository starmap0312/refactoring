# - a kind of duplicated code: two classes have similar methods but different interfaces
# - easy case: two classes perform identical functions but have different method names
# - root cause: the programmer who created a class probably didn't know that a functionally 
#   equivalent class already exists
# - use rename method, move method, parameterize method to make the signature and implementation
#   of methods identical, then delete one of the class
#   if only part of the functionality of the classes is duplicated, use extract superclass and
#   make the classes become sublcasses
# - after the refactoring, you get rid of the duplicated code and improve readability
