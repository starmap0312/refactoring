# - object-oriented code: lack of switch(or case) statement, use polymorphism instead
# - the problem of using switch statement: often the same switch statement appears at many places,
#   and adding or removing one case requires modifying many places, thus hard to extend the code
#   using polymorphism makes the code extension easier
# - when you see a switch statement, consider to use polymorphism
# - often the switch statement switches on a type code, so use "extract method" to extract
#   the switch statement and then move method to get it onto the class where the polymorphism is
#   needed
# - if polymorphism is overkill, then use replace parameter with explicit methods instead

# switch statement
if typeCode == '1':
    method1()
elif typeCode == '2':
    method2()
else:
    methodOther()

# use polymorphism: replace type code with subclasses
class TypeCode(object):
    # sublcasses implement different type code objects

    def method(self):
        raise NotImplementedError

class TypeCode1(TypeCode):
    # typeCode == 1 object

    def method(self):
        method1()

class TypeCode2(TypeCode)
    # typeCode == 2 object

    def method(self):
        method2()

class TypeCodeOther(TypeCode)
    # typeCode == other object

    def method(self):
        methodOther()


# use polymorphism: replace type code with state/strategy
class Client(object):
    # the class has a type code object(state/strategy), thus can change to other type code object
    # at run time

    def setTypeCode(self, typeCode):
        self.typeCode = typeCode

    def method(self):
        # use delegation to perform different type code behavior
        self.typeCode.method()

client = Client()
client.setTypeCode(TypeCode1())
