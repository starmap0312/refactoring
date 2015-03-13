# - shotgun surgery: to make a change, you need to make changes in many other places
# - parallel inheritance hierachies: a special case of shotgun surgery
#   every time you make a subclass of one class, you also need to make a subclass of another class
#   so the two classes are parallel in some sense in two separate inheritance hierachies
# - use move method and move field to make the changing happen at one single place(hierarchy)
