# - classes that have only fields, getting and setting methods for the fields, and nothing else
#   i.e. dumb data holders with no manipulation on the data
# - in early stages, you may use public fields for data classes
#   use encapsulate fields and encapsulate collections as early as possible
#   use remove setting method if a field is read-only(cannot be changed)
# - look for where the getting and setting methods are used and try to use move methods to
#   move behaviors into the data class
# - if you cannot move a whole method into the data class, try to use extract method first and
#   move part of the behavior into the data class; after that, you may find that you no longer
#   need the getting and setting methods, so you can use hide method on the getters and setters,
#   or use direct access to the fields and completely remove the getters and setters
# - it's ok to have data class at the beginning, but they better to take some responsibility later
#   while the code developing
