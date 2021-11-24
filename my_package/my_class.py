# Define a minimal class with an attribute
class MyClass:
    """A minimal example class
    :param text: text to set as the ``attribute`` attribute
    :ivar attribute: contains the contents of ``text`` passed in init
    """
    # Method to create a new instance of MyClass
    def __init__(self, value):
        # Define attribute with the contents of the value param
        self.attribute = value