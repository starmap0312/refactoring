# - if a subclass isn't doing much, then move all its features to superclass and then delete it
# - a superlcass and a subclass are not very different, then merge them together
# - use pull up field + pull up method, or push down field + push down method

# before
class Employee(object):
    # a superlcass

    def __init__(self):
        self._name = None

    def setName(self, name):
        self._name = name

    def getName(self):
        return self._name

class Salesman(Employee):
    # a subclass that isn't doing much

    def __init__(self):
        self._title = None

    def setTitle(self, title):
        self._title = title

    def getTitle(self):
        return self._title

salesman = Salesman()
salesman.setName('John')
salesman.setTitle('Mr.')
print salesman.getTitle(), salesman.getName()

# after: collapse heirarchy and merge the superclass and subclass
class Employee(object):
    # the subclass is merged into the superclass and then deleted

    def __init__(self):
        self._name = None
        self._title = None # pull up field

    def setName(self, name):
        self._name = name

    def getName(self):
        return self._name

    def setTitle(self, title):
        self._title = title # pull up method

    def getTitle(self):
        return self._title # pull up method

employee = Employee()
employee.setName('John')
employee.setTitle('Mr.')
print employee.getTitle(), employee.getName()
