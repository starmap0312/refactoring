# - an object has a field that is used only in certain circumstances, then it is difficult to
#   understand the code and figure out why the field is there
#   because we expect an object need all of its fields, not in special circumstances
# - use extract class to create a home for the poor orphan/temporary fields, and put all the
#   code related to the temporary fields in that extracted class
# - may use introduce null object to eliminate the conditional code regarding null case
# - temporary fields often happen when a complicated algorithm needs several fields
#   because you don't want to pass a huge parameter list, so you make them temporary fields
#   but the temporary fields are valid only during the algorithm, and can be confusing
#   in this case, you use extract class to take out all these variables and their related methods
#   the extracted class is then a method object
