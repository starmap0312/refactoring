# - builders of library classes are not omniscient, as they cannot figure out a design until
#   they've mostly built it
# - you are often restricted not to modify the library classes(you can't modify the source), 
#   ex. can't use move method or add a new method
# - introduce foreign method: if there are just a couple of methods that you wish to add
#   introduce local extension: if there is a whole load of extra methods(behaviors) that you
#   wish to add
