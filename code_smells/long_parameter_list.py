# - don't use global data(variables), as they are evil: pass in everything a fuction needs
#   as parameters(but this may result in a long parameter list)
# - in OOP, you don't need to pass everything the function needs, but instead you can pass in
#   objects so that the function can get what it needs by itself
# - use introduce parameter object/perserve whole object/replace parameter with method to
#   reduce the parameter list size
#   these also make changing parameter list easier
# - if a method can get a parameter value by other means, then it should get the value by itself
#   so that the parameter can be removed(reduce the parameter list size)
# - exception: if you don't want the dependency created, then pass in all the unpacked parameters
