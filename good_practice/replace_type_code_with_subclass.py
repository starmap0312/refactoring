# replace type code with subclass: if type code affects class behavior 
#   use sublcassing/polymorphism to handle the variant type-code related behavior
#   (if type code does not affect class behavior, replace type code with class instead)
# advantages
#   1) move knowledage of variant behavior from client to type subclass
#   2) easy to to add new variants (a new subclass): without polymorphism we need to change all the conditionals

# (after)
class EmployeeType(object):
    # type class has a type code

    (ENGINEER, SALESMAN, MANAGER) = (0, 1, 2) # type code

    def __init__(self):
        self._code = None
        self._monthlySalary = 50000
        self._commission = 1000000
        self._bonus = 300000        

    def getCode(self):
        return self._code         # can be moved downwards to subclasses

    def payAmount(self):
        raise NotImplementedError # imeplemented in subclasses

    @staticmethod
    def create(code):
        if code == EmployeeType.ENGINEER:
            return Engineer()
        elif code == EmployeeType.SALESMAN:
            return Salesman()
        elif code == EmployeeType.MANAGER:
            return Manager()
        else:
            raise Exception('Incorrect type code')

class Engineer(EmployeeType):
    # type-code subclass

    def __init__(self):
        super(Engineer, self).__init__()
        self._code = EmployeeType.ENGINEER

    def payAmount(self):
        return self._monthlySalary

class Salesman(EmployeeType):

    def __init__(self):
        super(Salesman, self).__init__()
        self._code = EmployeeType.SALESMAN

    def payAmount(self):
        return self._monthlySalary + self._commission

class Manager(EmployeeType):

    def __init__(self):
        super(Manager, self).__init__()
        self._code = EmployeeType.MANAGER

    def payAmount(self):
        return self._monthlySalary + self._bonus

# client
engineer = EmployeeType.create(EmployeeType.ENGINEER)
print engineer.payAmount()
manager = EmployeeType.create(EmployeeType.MANAGER)
print manager.payAmount()
# advantages
# 1) decouple type related behavior from client 
# 2) easy to create different type-code employees and behaviors
