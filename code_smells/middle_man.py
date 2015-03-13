# - you use hide delegate to hide the details of the delegate from the client(thus removing
#   the dependency of the client and the delegate): client -> server -> delegate
# - encapsulation: hide internal details from the rest of the world, so that it becomes easier
#   to make changes to the delegate 
# - however, use hide delegate will create middle man, and the overhead is the created
#   delegating methods(server class has delegating methods)
# - remove middle man: when the server class has half of its methods delegating to the delegate 
#   class, then the client can choose to talk to the delegate object directly
# - inline method: if a delegate object's method isn't doing much, then you may inline the method 
#   into the server/client class(reduce the number of delegating methods)
# - replace delegation with inheritance: when the server class behaves similarly to the
#   delegate class, you can use inheritance instead(make the server class a subclass of the 
#   delegate class). this allows you to extend behaviors without chasing all the delegations.
