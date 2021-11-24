class Parent:
    def __init__(self):
        self.parent_attribute = 'I am a parent'

    def parent_method(self):
        print('Back in my day...')

# Create a child class that inherits from Parent
class Child(Parent):
    def __init__(self):
        Parent.__init__(self)
        self.child_attribute = 'I am a child'

class SuperChild(Parent):
    def __init__(self):
        super().__init__()
        self.superchild_attribute = 'I am a superchild'

class GrandChild(SuperChild):
    def __init__(self):
        super().__init__()
        self.grandchild_attribute = 'I am a grandchild'