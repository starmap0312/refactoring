# - if a method is not used by other class, then make the method private
# - when you want to change your decision about the visibility of methods
# - a common case: you start with a data class, and then more and more behaviors are moved in
#   the data class, and finally you create a richer interface that provides high-level behaviors,
#   and then you find that you no longer need teh getting and setting method. Then you can
#   hide the getting and setting methods by making them private, or even more, you use direct
#   access to the class fields and completely remove the getting and setting methods

