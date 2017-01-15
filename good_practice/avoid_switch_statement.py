# - object-oriented code
#   lack of switch (or case) statement, use polymorphism instead
# - the problem of using switch statement
#   often the same switch statement appears at many places, and adding or removing one case requires
#     modifying many places, thus hard to extend the code
#   using polymorphism makes the code extension easier
# - when you see a switch statement, consider to use polymorphism
# - often the switch statement switches on a type code
#   use "extract method" to extract the switch statement and then move method to get it onto the class where
#   the polymorphism is needed
# - if polymorphism is overkill, then use replace parameter with explicit methods instead

# 1) switch statements
# client: tightly coupled to implementation
if typeCode == '1':
    method1()
elif typeCode == '2':
    method2()
else:
    methodOther()

# 2) explict methods: when polymorphism is overkill 
class TypeClass(object):
    # type-code class 

    def method1(self):
        method1()

    def method2(self):
        method2()

    def method_other(self):
        methodOther()

# client: loosely coupled to implementation
type = TypeClass()
type.method1()

# 3.1) polymorphism: replace type code with subclasses
class TypeClass(object):
    # type-code class 

    def method(self):
        raise NotImplementedError

class TypeClass1(TypeClass):
    # type-code subclass 

    def method(self):
        method1()

class TypeClass2(TypeClass)
    # type-code subclass 

    def method(self):
        method2()

class TypeClassOther(TypeClass)
    # type-code subclass 

    def method(self):
        methodOther()

# 3.2) polymorphism: replace type code with state/strategy
class Client(object):
    # wrapper class HAS_A type code object (state/strategy)

    def __init__(self, type):
        self.type = type

    def method(self):
        self.type.method() # a delegating method

# client: decoupled from implementation
client = Client(TypeClass1())
client.method()
