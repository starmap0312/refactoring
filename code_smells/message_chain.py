# - when a client asks one object for another object, which asks for yet another
# - remove dependency by using hide delegate in the message chain

# client
# message chain: you may see a sequnece of getter methods

class Person(object):

    def __init__(self, department):
        self._department = department

    def getDepartment(self):
        return self._department

class Department(object):

    def __init__(self, school):
        self._school = school

    def getSchool(self):
        return self._school

class School(object):

    def __init__(self, name):
        self._name = name

    def getName(self):
        return self._name


john = Person(Department(School('NTU')))
# the client is now coupled to the sequence of navigation: the client depends on class Department, 
# class School: any change to one of these classes may cause the client code to change
# client -> Person 
#        -> Department
#        -> School
print john.getDepartment().getSchool().getName() # get the school name

# use hide delegate to reduce the dependency
# ex. define the delegating method getName() in class Department
class Department(object):

    def __init__(self, school):
        self._school = school

    def getSchool(self):
        return self._school

    def getName(self):
        return self._school.getName()

john = Person(Department(School('NTU')))
# any change to class School does not affect the client code now
# client -> Person 
#        -> Department -> School
print john.getDepartment().getName()

# continue to use hide delegate to reduce the dependency
# ex. define the delegating method getName() in class Person
class Person(object):

    def __init__(self, department):
        self._department = department

    def getDepartment(self):
        return self._department

    def getName(self):
        return self._department.getName()

john = Person(Department(School('NTU')))
# any change to class Department does not affect the client code now
# client -> Person -> Department -> School
print john.getName()

# but this turns every intermediate object into a middle man
# an alternative is to use extract method to take a piece of the code that uses it and then
# use move method to push it down the chain
# so that the print getName() code is not performed at the client, but at the class School instead
