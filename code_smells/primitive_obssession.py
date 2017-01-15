# - two kinds of data: 
#   1) record type
#      structure data into meaningful groups (has overhead), ex. tables in a database
#   2) primitive type
#      your building blocks (built-in types)
# - write small objects (classes)
#   ex. class Money (number + currency)
#       class Range (upper_bound + lower_bound)
#       special strings like ZIP codes and phone numbers
# - from primitive data types to object-oriented data types
#   1) replace data value with object on individual data values
#   2) replace type code with class if the value does not affect behavior
#   3) use replace type code with subclasses or replace type code with state/strategy if
#      you have conditionals that depend on the type code
#   4) extract class if you have a group of fields that should go together
#   5) use introduce parameter object if you see these primitives in parameter lists
#   6) use replace array with object if you pick apart an array

