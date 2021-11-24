import my_package
from my_package.my_package import GrandChild

# Create instance of Child
child = my_package.Child()
super_child = my_package.SuperChild()
grand_child = my_package.GrandChild()

# Show attributes and methods of Child class
print(child.child_attribute)
print(child.parent_attribute)
# Show attributes of SuperChild and GrandChild
print(super_child.superchild_attribute)
print(grand_child.grandchild_attribute)

# Child inherits from parent method that belongs to Parent class 
child.parent_method()