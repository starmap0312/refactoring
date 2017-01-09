# - if an array acts as a data structure, make the data structure clearer by replacing the
# array with object
# - if the elements of an array means different things, define an object that has a field
# for each element
# - an array should contain a collection of "similar" objects in some order, don't use them
# to contain different things
# - the advantage is that you can use Move Method to add behavior to the new objects, and
# the code is easier to understand, with a better design

# Use Array, representing different things
row = ['Liverpool', '15']
name = row[0]
wins = int(row[1])
print name, wins

class Performance(object):
    # Convert into Object
    # if there are methods that constantly manipulate the fields, then consider to move 
    # the methods in, which adds behavior the the object

    def __init__(self):
        self._name = None
        self._wins = None

    def setName(self, name):
        self._name = name

    def getName(self):
        return self._name

    def setWins(self, wins):
        self._wins = wins

    def getWins(self):
        return int(self._wins)

# client code
row = Performance()
row.setName('Liverpool')
row.setWins('15')
print row.getName(), row.getWins()
