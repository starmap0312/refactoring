# replace parameterized method with explict methods
#   this improves readability (no need to look into the parameterized method)
# don't use explicit methods if the switch statement changes very often
#   use replace conditional with polymorphism instead, i.e. use subclasses and inheritance
#
# before: use parameterized method (lack of readability, need to look into the parameterized method)
class Rectangle(object):

    def __init__(self, h, w):
        self.height = h
        self.width = w

    def getValue(self, name):
        # this switch statement does not change too often
        if name == 'height':
            result = self.height
        elif name == 'width':
            result = self.width
        return result

rectangle = Rectangle(10, 20)
print rectangle.getValue('height')
print rectangle.getValue('width')

# after: use explict methods (more readable, if explicit methods change often, use subclassing and polymorphism)
class Rectangle(object):

    def __init__(self, h, w):
        self.height = h
        self.width = w

    def getHeight(self):
        return self.height

    def getWidth(self):
        return self.width

rectangle = Rectangle(10, 20)
print rectangle.getHeight()
print rectangle.getWidth()
