# - when the code is written with the classic two-tier approach to user interfaces and databases,
#   then try to isolate bussiness logic(database) from user interface code
# - when you have GUI classes that contain domain logic, then separate the domain logic into
#   a separate domain class: GUI class + domain class
# - MVC(model-view-controller): the separation between GUI(graphical user interface, the view or
#   presentation) and the domain logic(business logic, the model)
# - the separation makes the code easier to modify
# - allow multiple presentations(views) for the same business logic(model)
# - client-server GUIs use a logical two-tier design: the data in the database and the logic
#   in the presentation classes
# - separate the domain logic
#   1. move the domain logic fields into the domain class(move fields)
#   2. move the database logic(ex. SQL calls) to the domain class(extract method and move method)
# - the presentation(view) class HAS_A a domain logic object

# example
# GUI(the view, the presentation): the presentation class interacts with a relational database
class OrderWindow(object):
    # the presentation(view) class: contains all the behaviors, both for the GUI and for 
    # pricing the orders

    def __init__(self, order):
        self._order = order # HAS_A domain logic object

class Order(object):
    # the domain logic class(model): contains domain data and database logic
    pass

