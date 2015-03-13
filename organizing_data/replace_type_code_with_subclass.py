# - replace type code with subclass: if you have an immutable type code that affects the behavior 
#   of a class, i.e. use polymorphism to handle the variant behavior
# - the trigger to use replace type code with subclasses is the presence of conditional statements,
#   if there are no conditional statements, replace type code with class is better
# - advantage: move knowledage of variant behavior from clients of the class to the class itself
# - to add new variants, all one needs to do is add a subclass; without polymorphism one has to
#   find all the conditionals and change those 
# - useful when variants keep changing

class Employee(object):
    # the client class contains a type code, use subclasses to define type-code related
    # behaviors
    # limitation: the client object (subclass object) cannot change to other type-code
    # at run-time

    (ENGINEER, SALESMAN, MANAGER) = (0, 1, 2)

    def __init__(self):
        self._monthlySalary = 50000
        self._commission = 1000000
        self._bonus = 300000        

    def getType(self):
        # can also move this method downwards to subclasses which return constant values
        return self._type

    def payAmount(self):
        # allowing different behaviors to be defined in subclasses
        raise NotImplementedError

    @staticmethod
    def create(type):
        # create type-code subclass objects here
        if type == Employee.ENGINEER:
            return Engineer()
        elif type == Employee.SALESMAN:
            return Salesman()
        elif type == Employee.MANAGER:
            return Manager()
        else:
            raise Exception('Incorrect type code')

class Engineer(Employee):
    # the client has subclasses mapping to different type codes; therefore, allowing different 
    # behaviors to be defined in the subclass
    # limitation: cannot change to other subclass objects

    def __init__(self):
        super(Engineer, self).__init__()
        self._type = Employee.ENGINEER

    def payAmount(self):
        return self._monthlySalary

class Salesman(Employee):

    def __init__(self):
        super(Salesman, self).__init__()
        self._type = Employee.SALESMAN

    def payAmount(self):
        return self._monthlySalary + self._commission

class Manager(Employee):

    def __init__(self):
        super(Manager, self).__init__()
        self._type = Employee.MANAGER

    def payAmount(self):
        return self._monthlySalary + self._bonus

engineer = Employee.create(Employee.ENGINEER) # can create different type-code employees
print engineer.getType(), engineer.payAmount() # able to perform specific behavior

manager = Employee.create(Employee.MANAGER) # can create different type-code employees
print manager.getType(), manager.payAmount() # able to perform specific behavior
