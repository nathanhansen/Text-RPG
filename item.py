class Item():
    def __init__(self, item_name, item_description):
        """Creates a new item with a name and description."""
        self.name = item_name
        self.description = item_description
    
    def set_name(self, item_name):
        """Sets an item's name."""
        self.name = item_name

    def get_name(self):
        """Gets an item's name."""
        return self.name

    def set_description(self, item_description):
        """Sets an item's decription"""
        self.description = item_description
    
    def get_description(self):
        """Gets an item's description."""
        return self.description

    # Describe this item
    def describe(self):
        """This function prints an item's name and description to the shell."""
        print("There is a " + self.name + "lying in the room.")
        print(self.description )

    def get_details(self):
        """This function prints an item's name and descriptions to the shell."""
        print(self.name)
        print(self.description)