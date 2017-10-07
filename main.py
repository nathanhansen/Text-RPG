#############################################################
#Dork - the text-based RPG
#Author: Nathan Hansen
#Version: 1.0
#Date: 10.05.2017
#############################################################

from room import Room
from item import Item
from character import Character, Enemy, Friend

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

#start the player off in the kitchen with nothing in the backpack, no gold and three character to defeat
current_room = kitchen
backpack = ["teddy bear"]
gold = 100


#The game's loop. What makes it go
loop_tracker = True
while loop_tracker == True:		
    print("\n")
    print("You have defeated or helped " + str(miranda.get_status()) + " characters.")         
    if miranda.get_status() == 3:
        print("Congratulations!")
        print("You have defeated all of the challenges in Dork!")
        print("Now exiting.")
        break
    current_room.get_details()
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    loot = current_room.get_item()
    if loot is not None:
        loot.describe()
    
    #Get user input and check it against possible values
    command = input("> ")    
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
        else:
            print("There is no one here to talk to.")
    elif command == "fight":
        if inhabitant is not None:
            print("What will you fight with?")
            fight_with = input()
            loop_tracker = inhabitant.fight(fight_with)
        else:
            print("There is no one here to fight.")
    elif command == "bribe":
        if inhabitant is not None:
            print("How much gold will you attempt to bribe with?")     
            bribe_amount = int(input())
            if bribe_amount <= gold:
                gold -= bribe_amount
                loop_tracker = inhabitant.attempt_bribe(bribe_amount)
        else:
            print("There is no one here to bribe.")
    elif command == "gift":
        if inhabitant is not None:
            print("What will you give to " + inhabitant.name + "?")
            gift_given = input()
            if gift_given in backpack:
                inhabitant.give_gift(gift_given)
                backpack.remove(gift_given)
            else:
                print("You don't have that item.")
        else:
            print("There is no one here to give a gift to.")
    elif command == "take":
        if loot is not None:
            backpack.append(loot.get_name)
            current_room.set_item(None)
        else:
            print("There is nothing to take from this room.")
    elif command == "backpack":
        for item in backpack:
            print(item)
    elif command == "quit":
        print("Goodbye Dave...")
        loop_tracker = False
    elif command == "help":
        print("List of commands:")
        print("north, south, east, west")
        print("talk")
        print("fight")
        print("bribe")
        print("gift")
        print("take")
        print("backpack")
        print("quit")
    else:
        print("I didn't get that command...")
        
