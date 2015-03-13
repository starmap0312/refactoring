# - used to get rid of magic numbers
# - if the same logical number is referenced in more than one place, or it might ever change
# - improve readability


# before: if have a literal number with a particular meaning
def potentialEnergy(mass, height):
    return mass * 9.81 * height

# after: create a constant, use the meaning as its name
GRAVITATIONAL_CONSTANT = 9.81
def potentialEnergy(mass, height):
    return mass * GRAVITATIONAL_CONSTANT * height

# - if the magic number is a type code, use Replace Type Code with Class

