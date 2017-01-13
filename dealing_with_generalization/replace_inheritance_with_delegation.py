# - if subclass uses only part of superclass interface
#   if subclass does not want to inherit data
#     inheritance is not the natural relationship (will cause confusion to the reader)
#     so replace inheritance with delegation
# - sometimes, it is OK that subclass uses only part of superclass's data and behaviors,
#   as long as this does not cause confusion

# (before: use inheritance)
class Vector(object):
    # superclass

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
    # subclass

    def push(self, element): # additional (extended) behavior
        self.append(element)

    def pop(self):           # additional (extended) behavior
        result = self.remove(self.size()-1)
        return result

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print stack.pop(), stack.pop(), stack.pop()

# when subclass does not use all the methods of superclass
# (after: replace inheritance with delegation)
class Stack(object):
    # wrapper class

    def __init__(self):
        self._vector = Vector() # the delegate object

    def push(self, element):    # additional (extended) behavior
        self._vector.append(element)

    def pop(self):              # additional (extended) behavior
        return self._vector.remove(self.size()-1)

    def isEmpty(self):          # a delegating method
        return self._vector.isEmpty()

    def size(self):             # a delegating method
        return self._vector.size()

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print stack.pop(), stack.pop(), stack.pop()
