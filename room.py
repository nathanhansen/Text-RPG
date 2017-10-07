class Room():
    def __init__(self, room_name):
        """Creates a generic room and gives it a name."""
        self.name = room_name
        self.description = None 
        self.linked_rooms = {}
        self.character = None
        self.item = None

    def set_description(self, room_description):
        """Sets a room's description."""
        self.description = room_description

    def get_description(self):
        """Gets a room's description."""
        return self.description

    def set_name(self, room_name):
        """Sets a room's name."""
        self.name = room_name

    def get_name(self):
        """Gets a room's name."""
        return self.name

    def set_character(self, character):
        """Sets the character object for a room. A room can only contain one character."""
        self.character = character

    def get_character(self):
        """Returns the character object associated with a room."""
        return self.character

    def set_item(self, item):
        """Sets the item object associated with the room. A room can contain only one item."""
        self.item = item

    def get_item(self):
        """Returns the character object associated with a room."""
        return self.item

    def describe(self):
        """Prints the room's description to the shell."""
        print(self.description)

    def link_room(self, room_to_link, direction):
        """Associates the link between two rooms."""
        self.linked_rooms[direction] = room_to_link
        #print( self.name + " linked rooms :" + repr(self.linked_rooms) )

    def get_details(self):
        """Prints the name, description, and linked rooms for the specified room object."""
        print(self.name)
        print(self.description)
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print( "The " + room.get_name() + " is " + direction)
        print("---------------" + "\n")

    def move(self, direction):
        """Allows the player to move between two linked rooms. Returns an error message if not successful."""
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self
