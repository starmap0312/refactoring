# - when you do too much for generality
#     ex. create abstract classes for no reason
#     ex. create class hierarchy to handle special cases that are not required yet
#     ex. add parameter to method that is not needed
#   then the code becomes difficult to understand and maintain
# - useless abstract classes: use collapse hierarchy to remove them
#   unnecessary delegation: use inline class to merge the two classes into one
#   unused parameters: use remove parameter
#   too abstract method name: use rename method to show its purpose

