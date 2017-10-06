from room import Room
from item import Item
from character import Enemy, Friend

#Let's create some rooms!
#First up is the kithen
kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")

#Then the ballroom
ballroom = Room("Ballroom")
ballroom.set_description("A classy room filled with game tables, books and booze.")

#Finally the dining room
dining_hall = Room("Dining Hall")
dining_hall.set_description("A long and wide room filled with tables, chairs and the half-eaten remains of dinner.")

#Create the links between the rooms
kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

#Let's add items to the rooms
cheese = Item("cheese", "A large hunk of golden cheddar")
kitchen.set_item(cheese)
longsword = Item("longsword", "A long bladed weapon with a leather grip")
dining_hall.set_item(longsword)

#Create some characters to interact with and place them in their own room
#Your friend Miranda, who owns the house and provides some hints
miranda = Friend("Miranda", "The home's owner. An elegant woman sitting at the kitchen table.")
miranda.set_conversation("Well met, adventurer. What brings you to my humble home? Have you found my lost teddy bear?")
miranda.set_gift("teddy bear")
miranda.set_gift_conversation("To defeat the zombie in the next room you need some cheese. This is a kitchen so there should be some.")
kitchen.set_character(miranda)

#Dave is a zombie, unfortunately
dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Brrlgrh... rgrhl... brains...")
dave.set_weakness("cheese")
dining_hall.set_character(dave)

#These kinds of text adventures need an orc
reggie = Enemy("Reggie", "A hideous orc covered in scars")
reggie.set_conversation("Me no like you! But me no wanna fight you? What you life worth?")
reggie.set_weakness("longsword")
reggie.set_bribe(100)
ballroom.set_character(reggie)

#start the player off in the kitchen with nothing in the backpack
current_room = kitchen
backpack = []
tracker = True          

#The game's loop. What makes it go
while tracker == True:		
    print("\n")         
    current_room.get_details()
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    loot = current_room.get_item()
    if loot is not None:
        loot.describe()
    command = input("> ")    
    # Check what was typed
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    elif command == "talk":
        inhabitant.talk()
    elif command == "fight":
        print("What will you fight with?")
        fight_with = input()
        tracker = inhabitant.fight(fight_with)
    elif command == "bribe":
        print("How much gold will you attempt to bribe with?")
        bribe_amount = int(input())
        tracker = inhabitant.attempt_bribe(bribe_amount)
    elif command == "gift":
        print("What will you give to " + inhabitant.name + "?")
        gift_given = input()
        inhabitant.give_gift(gift_given)
    elif command == "take"
        backpack.append(loot.get_name)
        current_room.set_item(None)
    else:
        print("I didn't get that command...")
        
