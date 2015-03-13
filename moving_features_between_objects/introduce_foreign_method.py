# - if a server class needs an additional method, but you can't modify the class(ex. can't
#   use move method as it is a library class), then you create a method in the client class
#   with an instance of the server class as its first argument

# before: client -> server
class Server(object):
    # the server class, which you are forced to not edit(ex. it is a library class)

    def __init__(self, year, month, date):
        self._year = year
        self._month = month
        self._date = date

    def getYear(self):
        return self._year

    def getMonth(self):
        return self._month

    def getDate(self):
        return self._date

    # cannot add a new method as follows
    def getNextDay(self):
        return '%s/%s/%s' % (self.getYear(), self.getMonth(), self.getDate()+1)

# client
server = Server(2015, 4, 18)
print server.getNextDay()

# after: client with a foreign method -> server
# add a new method at the client class and pass the server object as its parameter
# although the method operates on the server class's data, you're restricted to not move 
# the method into the server class. in this case, the new method is a foreign method of the server
# class
def getNextDay(server):
    return '%s/%s/%s' % (server.getYear(), server.getMonth(), server.getDate()+1)

print getNextDay(server)
