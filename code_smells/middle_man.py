# - hide delegate / encapsulation
#   pros:
#         client -> wrapper -> delegate
#         decouples client from delegate, hide the details of delegate from client
#         hide internal details from rest of the world, so it becomes easier to make changes to delegate 
#   cons:
#         create middle man, additional delegating methods (wrapper class has delegating methods)
# - remove middle man (wrapper)
#   when wrapper class has half of its methods delegating to delegate class
#   client can choose to talk to the delegate object directly
# - replace delegation with inheritance
#   when wrapper class behaves similarly to the delegate class
#   replace delegation with inheritance (make the wrapper class a subclass of the delegate class)
#   pros:
#     easily extend behaviors without chasing all the delegations (add a subclass)
#   cons:
#     client is coupled to subclasses
#     subclasses are coupled together due to inheritance
# - inline method
#   if delegate object's method isn't doing much, then inline the method into the wrapper/client class
#   this reduces the number of delegating methods
