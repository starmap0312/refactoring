# - when a class is trying to do too much: ex. if a class has too many variables, then try
#   to extract related variables into a new class(or subclass)
# - if a class does not use all of its variables all of the time, then try to use extract class
#   or extract subclass
# - observe how the client uses the large class, and then first apply extract interface for each
#   of these uses
# - after that, you may be able to further break up the class by extract class or extract subclass
