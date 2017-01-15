# - group related data items together
#   if you see some data items together in many places:
#   ex. fields in a couple of classes, or parameters in many methods, make them into their own object
# - use extract class to pull out the related fields into an object, this reduces the field list
#   then apply introduce parameter object or preserve whole object to reduce the parameter list 
#   size of methods
# - reducing field list or parameter list could remove a few bad smells. after that, look for
#   cases of feature envy and to move related behaviors(move methods) to the new data object
# - a good test to see what data items go together: delete one of the field, and then see if
#   the remaining make any sense
