# - inappropriate intimacy: when classes are far too intimate and spend too much time delving
#   in each others's private parts
# - use move method and move field to reduce the intimacy
# - if the classes have common interests, use extract class to put the commonality in one place
# - use hide delegate to make another class as a middle man, so that the two intimate classes
#   do not interact with each other directly
# - use replace inheritance with delegation: inheritance often leads to overintimacy, as 
#   sublcasses easily know more about their parents than their parents would like them to know
# - use change bidirectional association to unidirectional to reduce intimacy: drop the unneeded
#   end of the association(if one class no longer needs features of the other class)
