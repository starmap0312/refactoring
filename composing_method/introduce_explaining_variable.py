# - if have a complicated expression that is hard to understand, put the result of the expression
#   or parts of the expression in a temp variable with a name explaining its purpose
# - an alternative is to use extract method, but sometimes extract method is hard, 
#   because there are too many local temp variables then use introduce explaining variables

platform = 'MAC'
browser = 'IE'
# before: long expression
if platform.upper().index('MAC') > -1 and browser.upper().index('IE') > -1:
    print 'MAC and IE'

# after: use temp variables to explain parts of the expression
isMac = platform.upper().index('MAC') > -1
isIE = browser.upper().index('IE') > -1
if isMac and isIE:
    print 'MAC and IE'

# use extract method instead

def isMac(platform):
    return platform.upper().index('MAC') > -1

def isIE(browser):
    return browser.upper().index('IE') > -1

if isMac(platform) and isIE(browser):
    print 'MAC and IE'
