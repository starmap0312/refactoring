# - if there are identical constructors in subclasses
#   you can pull up to superclass constructor and call superclass constructor from subclass constructor
# - if see common behaviors in normal methods of subclasses, consider to pull them up to superclass
#   ex. if the common behaviors are in constructors, you need to pull them up to superclass contructors
#        you need to call them from subclass constructors unless the subclass construction does nothing

# before: identical constructors in subclasses

class Employee(object):

    def __init__(self):
        self._name = None
        self._id = None

class Manager(Employee):
    # subclass

    def __init__(self, name, id, grade):
        self._name = name
        self._id = id
        self._grade = grade

class Engineer(Employee):
    # subclass

    def __init__(self, name, id, grade):
        self._name = name
        self._id = id
        self._grade = grade

engineer = Engineer('John', '15321', '85')
print engineer._name, engineer._id, engineer._grade

# after: pull up constructor to superclass 
class Employee(object):
    # superclass

    def __init__(self, name, id):
        self._name = name
        self._id = id

class Engineer(Employee):
    # subclass

    def __init__(self, name, id, grade):
        super(Engineer, self).__init__(name, id)
        self._grade = grade


engineer = Engineer('John', '15321', '85')
print engineer._name, engineer._id, engineer._grade

