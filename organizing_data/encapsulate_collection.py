# - encapsulate field packs a simple data type, whereas encapsulate collection packs a complex
#   collection type
# - before: a method returns a collection; after: make it return a read-only view and provide
#   add/remove methods
# - the collection might be an array, list, set, or vector; the getter should not return
#   the collection object itself, because that allows clients to manipulate the contents of
#   the collection without the owning class's knowing what is going on. this reveals too much
#   to the clients about the collection object's internal data structures
# - the getter should hide unnecessary details about the collection object's structure
# - the setter for collection: there should be operations to add and remove elements. this gives
#   the owning object control over adding and removing elements from collection
# - advantage: the collection is properly encapsulated, reducing the coupling of the owining class
#   to its clients: eaiser to extend because of the less coupling

# exmaple: encapsulating sets
# (before)
class Course(object):

    def __init__(self, name, isAdvanced):
        self._name = name # string
        self._isAdvanced = isAdvanced # boolean

    def getName(self):
        return self._name

    def isAdvanced(self):
        return self._isAdvanced

class Person(object):
    # owning class of the collection object

    def __init__(self):
        self._courses = set()

    def getCourse(self):
        # get the collection object directly
        return self._courses

    def setCourse(self, courses):
        self._courses = courses

# client of the owining class get and manipulate the collection object directly
kent = Person()
courses = kent.getCourse()
courses.add(Course('Python Programming', False))
courses.add(Course('Algorithm', False))
courses.add(Course('Machine Learning', True))
for course in kent.getCourse():
    print course.getName(), course.isAdvanced()

# (after) encapsulate collection

class NewPerson(object):
    # make the collection object read-only and provide add/remove methods(getter/setter)
    # no one can change the collection object, unless through add/remove methods
    # further, move collection object related behaviors into the class
    # in practice, moving collection related behaviors into class will not lead to bloated class

    def __init__(self):
        self._courses = set() # private, cannot be accessed directly

    def addCourse(self, course):
        self._courses.add(course)

    def removeCourse(self, course):
        self._courses.remove(course)

    def initializeCourses(self, courses):
        assert not self._courses # assert collection object is empty
        for course in courses:
            self.addCourse(course)

    def getCourses(self):
        # return the read-only collection object
        return frozenset(self._courses)

    def numberOfCourses(self):
        return len(self._courses)

    def numberOfAdvancedCourses(self):
        count = 0
        for course in self.getCourses():
            if course.isAdvanced():
                count += 1
        return count

# client code
john = NewPerson()
courses = set()
c = Course('Python Programming', False)
courses.add(c)
courses.add(Course('Algorithm', False))
john.initializeCourses(courses)
john.addCourse(Course('Machine Learning', True))
john.removeCourse(c)
for course in john.getCourses():
    print course.getName(), course.isAdvanced()
# john.getCourses().add(Course('AI', True)) # the collection object is read-only
print 'number of courses: %s' % john.numberOfCourses()
print 'number of advanced courses: %s' % john.numberOfAdvancedCourses()

# exmaple: encapsulating arrays
# in practice, rarely use arrays, instead use more behaviorally rich collections

class NewNewPerson(object):

    def __init__(self):
         self._skills = []

    def setSkill(self, index, skill):
        self._skills[index] = skill

    def initializeSkills(self, skills):
        for skill in skills:
            self._skills.append(skill)

    def getSkills(self):
         # return a copy of the collection object, since the collection object should be read-only
         copy = list(self._skills)
         return copy

# client code
skills = ['Python', 'C/C++', 'Java']
person = NewNewPerson()
person.initializeSkills(skills)
person.setSkill(1, 'Design Pattern')
for skill in person.getSkills():
    print skill, '/',
