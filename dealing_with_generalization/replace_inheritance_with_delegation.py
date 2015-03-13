# - when a subclass uses only part of a superclass's interface or does not want to inherit data,
#   then remove subclassing and use delegation instead
#   in this case, use subclassing will cause confusion to the reader
# - you may start with using subclassing first, but later find that the subclass does not want
#   many of the superclass's operations. in this case, the superclass's interface is not a
#   true reflection of what the subclass does, and can cause confusion to the reader
# - or you may find that the subclass is inheriting a whole load of data that is not appropriate
#   for the subclass(or do not make sense in the subclass), then remove subclassing and use
#   delegation
# - but often, it is OK that a subclass uses only part of the superclass's data and behaviors,
#   as long as this does not cause confusion
# - using delegation means that you're making use of only part of the delegated class, thus no
#   confusion at all; but the overhead is the adding of delegating methods
#   using delegation you can control what aspects of the interface to use and what to ignore

# before: subclassing
class Vector(object):

    def __init__(self):
        self._vector = []

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return len(self._vector)

    def append(self, element):
        self._vector.append(element)

    def remove(self, index):
        element = self._vector[index]
        self._vector.remove(element)
        return element

class Stack(Vector):

    def push(self, element):
        self.append(element)

    def pop(self):
        result = self.remove(self.size()-1)
        return result

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print stack.pop(), stack.pop(), stack.pop()

# after: remove inheritance and use delegation
class NewStack(object):

    def __init__(self):
        self._vector = Vector()

    def push(self, element):
        self._vector.append(element)

    def pop(self):
        return self._vector.remove(self.size()-1)

    def isEmpty(self):
        return self._vector.isEmpty()

    def size(self):
        return self._vector.size()

stack = NewStack()
stack.push(1)
stack.push(2)
stack.push(3)
print stack.pop(), stack.pop(), stack.pop()
