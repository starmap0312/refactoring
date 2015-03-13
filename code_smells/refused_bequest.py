# - subclasses inherit all the data and methods of the superclasses, but sometimes they don't
#   want or need what they inherit
# - traditional way: create two sibling classes and use push down method and push down
#   field to push all unused methods to one of the sibling class
#   but you don't need to do this all the time, because doing this also increases the complexity
#   of the hierarchy
# - most of the time sublcassing is just to reuse the code of the superclass(part of its behaviors)
#   so it is OK, if a subclass does not intend to use all the inherited data and methods
#   that is, the refused bequest is usually not a strong smell
# - the smell becomes stronger when the subclass causes confusion: ex. if a subclass reuses
#   part of the behaviors of its superclass but does not want to support the interface of the
#   superclass. in this case, subclassing is not a good idea, and we may use replace inheritance 
#   with delegation instead(when a subclass uses only part of a superclass's interface or
#   does not want to inherit data)
