# - when a tangled inheritance hierarchy combines sereval variations in a confusing way
# - when you have an inheritance hierarchy that is doing two jobs at once, then create two
#   hierarchies and use delegation to invoke one from the other
# - doing two jobs with one hierarchy: one hierarchy should reflect one kind of job variations

# bad design: two job responsibilities are mixed in one hierarchy
#             you begin with job1 variations, but some time later you directly add job2 extentions
#             by subclassing, which leads to the following bad design hierarchy
# dual -> job1 variation(subclass) -> job2 variation(subclass)
#      -> job1 variation(subclass) -> job2 variation(subclass)
# as two jobs are mixed in the hierarchy,
# 1. the code is hard to understand: the hierarchy does not produce one result, but two kinds of
#    results
# 2. code duplication: you may write the same job2 code in the hierarchy
# 3. the code is hard to change: if you want to add subclasses for job2, you need to change
#    many places as job2 subclasses are spread around in the hierarchy

# better design:
# job1 superclass -> job1 variation(subclass)
#                 -> job1 variation(subclass)
# job2 superclass -> job2 variation(subclass)
#                 -> job2 variation(subclass)
# job1 object HAS-A job2 object(use delegation)

# identify the two job responsibilities, and then use extract class, move fields, and move methods
# to separate them into two different hierarchies
# let the more important job be the main object, which has a reference to the other job object
# i.e. use delegation for the less important job

