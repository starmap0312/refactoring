# - if a temp variable is assigned to more than once (not a loop varaible nor a collecting 
#   variable), create temp variables for each assignment
#   this makes the code clearer, each temp variable has only one responsibility
# - each temp variable has only one responsibility in a method
#   using a temp variable for two different things is very confusing
# - variable can be set twice only if it's a loop variable or a collecting (summing) variable

# before: a temp varialbe is used for two purposes
height = 5
width = 10
temp = 2 * (height + width) # temp is assigned
print temp
temp = height * width # temp is assigned
print temp

# after: the intention of the temp variable becomes more clear
perimeter = 2 * (height + width) # first temp variable
print perimeter
area = height * width # second temp variable
print area
