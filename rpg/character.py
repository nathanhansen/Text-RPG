class Character():
    victory_count = 0

    # Create a character
    def __init__(self, char_name, char_description):
        """Creates a new character with a name and a description."""
        self.name = char_name
        self.description = char_description
        self.conversation = None
        self.bribe = None

    # Describe this character
    def describe(self):
        """Prints the name of the character and its description."""
        print( self.name + " is here!" )
        print( self.description )

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        """Sets the conversation string for a character."""
        self.conversation = conversation

    def set_bribe(self, bribe_amount):
        """Sets the bribe amount for a character."""
        self.bribe = bribe_amount

    def get_bribe(self):
        """Returns acharacter's bribe amount."""
        return self.bribe

    # Talk to this character
    def talk(self):
        """If a conversation string has been set prints the conversation to the player."""
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, combat_item):
        """Generic characters and Friend characters will not fight with the player."""
        print(self.name + " doesn't want to fight with you")
        return True

    # Determine how many characters have been helped or defeated
    def get_status(self):
        """Returns the integer value of how many characters have been helped or defeated."""
        return Character.victory_count

#A subclass of character for enemy NPCs
class Enemy(Character):
    def __init__(self, char_name, char_description):
        """Creates an enemy type character."""
        super().__init__(char_name, char_description)
        self.weakness = None

    def set_weakness(self, weakness):
        """Sets an enemies weakness for use when fighting them."""
        self.weakness = weakness

    def get_weakness(self):
        """Returns the set weakness of an enemy."""
        return self.weakness

    def fight(self, combat_item):
        """This function allows the player to fight an enemy. 
        If he has the correct item, the enemy is defeated and the victory counter in incremented. 
        Otherwise, the returned value will end the game."""
        if combat_item == self.weakness:
            print("You fend " + self.name + " off with the " + combat_item )
            Character.victory_count +=1
            return True
        else:
            print(self.name + " crushes you, puny adventurer")
            return False

    def attempt_bribe(self, bribe_amount):
        """Allows the player to attempt a bribe of an enemy. Success increases the victory counter.
        Failure leads to a fight with the enemy."""
        if bribe_amount >= self.bribe:
            print("You have bribed " + self.name + "with " + str(bribe_amount) + " gold.")
            Character.victory_count +=1
            return True
        else:
            print(self.name + "was not impressed with your bribe and attacks!")
            print("What will you fight with?")
            fight_with = input()
            return self.fight(fight_with)

#A subclass of character for your friends. But with friends like these, who needs enemies?
class Friend(Character):
    def __init__(self, char_name, char_description):
        """Creates a new friend character."""
        super().__init__(char_name, char_description)
        self.gift = None
        self.gift_conversation = None
    
    def set_gift(self, gift_name):
        """Sets the gift needed for a friend character."""
        self.gift = gift_name

    def get_gift(self):
        """Returns the gift needed for a friend character."""
        return self.gift

    def set_gift_conversation(self, conversation_string):
        """Sets the gift conversation for a friend character"""
        self.gift_conversation = conversation_string
    
    def get_gift_conversation(self):
        """Gets a friend characters gift conversation."""
        return self.gift_conversation

    def give_gift(self, gift_name):
        if gift_name == self.gift:
            """Attempts to give a gift to a friend character.
            If successful, the character gives a helpful hint.
            No harm if the character is not interested."""
            print(self.name + "accepts the gift and thanks you.")
            print("[" + self.name + " says]: " +self.gift_conversation)
            Character.victory_count +=1
            self.set_conversation = self.gift_conversation
            return True
        else:
            print(self.name + "is not interested in this item. Sorry.")


