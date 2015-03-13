# - used when classes have too much behavior or when classes are collaborating too much and
#   are too highly coupled
# - move method: make classes simpler
# - if a method references another object more than the object it lives on, consider to move it
# - if it is hard to make the decision, then it probably does not matter that much

# before move method
class Account(object):
    # the responsibility of the computation of overdraftCharge is in class Account

    def __init__(self):
        self._type = None
        self._daysOverdrawn = None

    def overdraftCharge(self):
        # depends on self._type and self._daysOverdrawn to compute the charge
        if self._type.isPremium():
            result = 10
            if self._daysOverdrawn > 0:
                result += (self._daysOverdrawn - 7) * 0.85
            return result
        else:
            return self._daysOverdrawn * 1.75

    def bankCharge(self):
        # depends on self._daysOverdrawn and calls self.overdraftCharge()
        result = 4.5
        if self._daysOverdrawn > 0:
            result += self.overdraftCharge()
        return result

# after move method
class AccountType(object):
    # move the computation of overdraftCharge() into AccountType

    def overdraftCharge(self, daysOverdrawn):
        # pass the feature variable, i.e. daysOverdrawn, as a parameter
        if self.isPremium():
            result = 10
            if daysOverdrawn > 7:
                result += (daysOverdrawn - 7) * 0.85
            return result
        else:
            return daysOverdrawn * 1.75

    def overdraftCharge(self, account):
        # can also pass the source object, Account object, as a parameter
        # useful when overdraftCharge() calls another method on the account
        if self.isPremium():
            result = 10
            if account.getDaysOverdrawn() > 7:
                result += (account.getDaysOverdrawn() - 7) * 0.85
            return result
        else:
            return account.getDaysOverdrawn() * 1.75

class Account(object):
    # remove method overdraftCharge, or use simple delegation: need to check all the callers

    def __init__(self):
        self._type = None
        self._daysOverdrawn = None

    def bankCharge(self):
        # depends on self._daysOverdrawn and self._type
        result = 4.5
        if self._daysOverdrawn > 0:
            result += self._type.overdraftCharge(self._daysOverdrawn)
        return result
