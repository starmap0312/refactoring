# - problem: inappropriate intimacy
#   when classes are far too intimate and spend too much time delving in each others's private parts
# - soluiton
#   1) extract class, move method, move field
#      if the classes have common interests, put the commonality in one place (class)
#   2) replace inheritance with delegation
#      use hide delegate to make another class as a middle man, so that the two intimate classes
#        do not interact with each other directly
#      inheritance often leads to overintimacy, as 
#        sublcasses easily know more about their parents than their parents would like them to know
#   3) change bidirectional association to unidirectional
#      drop the unneeded end of the association if one class no longer needs features of the other class
