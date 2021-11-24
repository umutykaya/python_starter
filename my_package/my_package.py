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

# class SuperChildClass(Parent):
#     def __init__(self):
#         super().__init__()
#         print("I'm a super child!")

# class GrandChildClass(SuperChild):
#     def __init__(self):
#         super().__init__()
#         print("I'm a grandchild!")