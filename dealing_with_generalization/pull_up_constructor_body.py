# - if have identical constructors on subclasses, then pull up by creating a superclass constructor
#   call the superclass constructor from the subclass constructor
# - if see common behaviors in normal methods of subclasses, consider to pull them up to superclass
#   but if the common behaviors are in constructors, you need to pull them up to superclass
#   contructors. very often you need to call them from subclass constructors unless the 
#   subclass construction does nothing

# before

class Employee(object):

    def __init__(self):
        self._name = None
        self._id = None

class Manager(Employee):

    def __init__(self, name, id, grade):
        self._name = name
        self._id = id
        self._grade = grade

class Engineer(Employee):

    def __init__(self, name, id, grade):
        self._name = name
        self._id = id
        self._grade = grade

# after
class NewEmployee(object):

    def __init__(self, name, id):
        self._name = name
        self._id = id

class NewEngineer(NewEmployee):

    def __init__(self, name, id, grade):
        super(NewEngineer, self).__init__(name, id)
        self._grade = grade

engineer = Engineer('John', '15321', '85')
print engineer._name, engineer._id, engineer._grade

newengineer = NewEngineer('John', '15321', '85')
print newengineer._name, newengineer._id, newengineer._grade

