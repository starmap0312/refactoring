# - we want to structure our code to make change easier
#   it is better if we can jump to a single clear point to make the change
# - divergent change: when a class is commonly changed in different ways for different reasons
#   it is better if one class is changed only as a result of one kind of change, so if a class
#   is often changed for two reasons, it is better to make it into two separate classes
# - use extract class to pull all parts of a class that relates to a change together
#   ex: a change that happens when adding a new database, or a change that happens when adding
#   a new financial instrument

