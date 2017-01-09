# - to interface with a record structure, ex. database record
#   create an interfacing class to deal with the external element, ex. database record
# - create a dummy data object without any behavior, extra behaviors will be added or move in later

# DB columns: Name, Age, Gender, Job
record = ['Bob', 32, 'Male', 'Engineer']

class Record(object):
    # a dumb class, behaviors will added later during development

    def __init__(self, name, age, gender, job):
        self.name = name
        self.age = age
        self.gender = gender
        self.job = job

record = Record('Bob', 32, 'Male', 'Engineer')
print record.name, record.age, record.gender, record.job
