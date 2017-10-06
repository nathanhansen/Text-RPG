class Character():

    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    # Describe this character
    def describe(self):
        print( self.name + " is here!" )
        print( self.description )

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True

#A subclass of character for enemy NPCs
class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None
        self.bribe = 0

    def set_weakness(self, weakness):
        self.weakness = weakness

    def get_weakness(self):
        return self.weakness

    def set_bribe(self, bribe_amount):
        self.bribe = bribe_amount

    def get_bribe(self):
        return self.bribe

    def fight(self, combat_item):
        if combat_item == self.weakness:
            print("You fend " + self.name + " off with the " + combat_item )
            return True
        else:
            print(self.name + " crushes you, puny adventurer")
            return False

    def attempt_bribe(self, bribe_amount):
        if bribe_amount >= self.bribe:
            print("You have bribed " + self.name + "with " + str(bribe_amount) + " gold.")
            return True
        else:
            print(self.name + "was not impressed with your bribe and attacks!")
            print("What will you fight with?")
            fight_with = input()
            return self.fight(fight_with)

#A subclass of character for your friends. But with friends like these, who needs enemies?
class Friend(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.gift = None
        self.gift_conversation = None

    def set_bribe(self, bribe_amount):
        self.bribe = bribe_amount

    def get_bribe(self):
        return self.bribe

    def set_gift(self, gift_name):
        self.gift = gift_name

    def get_gift(self):
        return self.gift

    def set_gift_conversation(self, conversation_string):
        self.gift_conversation = conversation_string
    
    def get_gift_conversation(self):
        return self.gift_conversation

    def give_gift(self, gift_name):
        if gift_name == self.gift:
            print(self.name + "accepts the gift and thanks you.")
            print("[" + self.name + " says]: " +self.gift_conversation)
            return True
        else:
            print(self.name + "is not interested in this item. Sorry.")


