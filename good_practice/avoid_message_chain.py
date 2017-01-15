# problem
#   when a client asks one object for another object, which asks for yet another object
# solution
#   remove dependency by hiding delegate in the message chain
#
# (before: message chain, use a sequnece of getter methods)

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

# client -> Person 
#        -> Department
#        -> School
# client is coupled to the sequence of navigation
john = Person(Department(School('NTU')))
print john.getDepartment().getSchool().getName()

# (after: hide delegate to reduce the dependency)

class Person(object):

    def __init__(self, department):
        self._department = department

    def getDepartment(self):
        return self._department

    def getName(self):                    # a delegating method#
        return self._department.getName()

class Department(object):

    def __init__(self, school):
        self._school = school

    def getSchool(self):
        return self._school

    def getName(self):                    # a delegating method
        return self._school.getName()

# client -> Person -> Department -> School
# decouple client from subclasses 
john = Person(Department(School('NTU')))
print john.getName()
