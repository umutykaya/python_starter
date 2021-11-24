class Parent:
    def __init__(self):
        """
        Parent Class
        :return: parent_attribute <str>
        """
        self.parent_attribute = 'I am a parent'

    def parent_method(self):
        """
        Parent Class
        :return: partner_attribute <str>
        To call the `parent_method()` use following line:
        >>> child.parent_method()
        """
        self.partner_attribute = 'Back in my day...'

# Create a child class that inherits from Parent
class Child(Parent):
    def __init__(self):
        """
        Child Class
        :return: child_attribute <str>
        """
        Parent.__init__(self)
        self.child_attribute = 'I am a child'

class SuperChild(Parent):
    def __init__(self):
        """
        SuperChild Class
        :return: superchild_attribute <str>
        """
        super().__init__()
        self.superchild_attribute = 'I am a superchild'

class GrandChild(SuperChild):
    def __init__(self):
        """
        GrandChild Class
        :return: grandchild_attribute <str>
        """
        super().__init__()
        self.grandchild_attribute = 'I am a grandchild'