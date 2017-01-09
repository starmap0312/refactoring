# - replace an algorithm with one that is clearer

# before
def foundPerson(people):
    for i in range(len(people)):
        if people[i] == 'Don':
            return 'Don'
        if people[i] == 'John':
            return 'John'
        if people[i] == 'Kent':
            return 'Kent'
    return ''

# after
def foundPerson2(people):
    candidates = ['Don', 'John', 'Kent']
    for i in range(len(people)):
        if people[i] in candidates:
            return people[i]
    return ''

print foundPerson(['Alice', 'Bob', 'John', 'Tom'])
print foundPerson2(['Alice', 'Bob', 'John', 'Tom'])
