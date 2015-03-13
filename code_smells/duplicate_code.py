# - duplicate code: try to unify the same code structure
# - extract method: if same expression appear in two methods of the same class/namespace/module
#   extract method + pull up field: if same expression appear in two methods of sibling
#   subclasses
#   extract method + pull up to higher layer module/namespace: if same expression appear in two
#   different modules/namespaces
# - form template method: if two methods in the same class(or sibling classes) have the same code 
#   structure but different implementations
# - extract class: if same code structure exists in two unrelated classes, then use extract class
#   in one class and then use the extracted class in the other class
