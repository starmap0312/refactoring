# - the reverse of parameterize method
# - if a method runs different code depending on the values of an enumerated parameter, then
#   create a separate method for each value of the parameter
# - don't use explicit methods if the switch statement changes very often: use replace conditional
#   with polymorphism instead(i.e. subclasses and inheritance)

# before
class Rectangle(object):
    # a class with parameterized method(having switch statement): different values do different
    # things

    def __init__(self):
        self.height = None
        self.width = None

    def setValue(self, name, value):
        # a parameterized method: if this switch statement does not change too often, you can
        # replace parameter with explicit methods to eliminate the switch statement
        # decide at run time, no compile time checking
        if name == 'height':
            self.height = value
        elif name == 'width':
            self.width = value

# lack of readability: often requires documentation or look into the parameterized method
rectangle = Rectangle()
rectangle.setValue('height', 10) # pass in different name to do different setting
rectangle.setValue('width', 20) # pass in different name to do different setting
print rectangle.height, rectangle.width

# after
class Rectangle(object):
    # a class without parameterized method(replaced with explicit methods)

    def __init__(self):
        self.height = None
        self.width = None

    def setHeight(self, value):
        # an explicit method: gain complie time checking
        self.height = value

    def setWidth(self, value):
        # an explicit method: gain complie time checking
        self.width = value

# the code is easier to read: no needs to look into the method
rectangle = Rectangle()
rectangle.setHeight(10) # call different explicit method
rectangle.setWidth(20) # call different explicit method
print rectangle.height, rectangle.width
