# - a method's body is as clear as its name, then you can remove the method, and replace it
#   with its body directly
# - when a group of methods seem badly factored, then inline them and refactor again
#   this often happens before try to use replace method with method object

# before
def getRating():
    return 2 if moreThanFiveLateDeliveries() else 1

def moreThanFiveLateDeliveries():
    return _numberOfLateDeliveries > 5

# after: remove the method, and replace with its body
def getRating():
    return 2 if _numberOfLateDelivers > 5 else 1
