# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 09:23:43 2022

@author: Kaala
whtsp    
+  8 8 01 79 34     51237
"""
import random # For generating random numbers
import os # For clear the terminal or command prompt

# Rooms have items, players can carry items
class Item:

    def __init__(self, name='Unknown'):
        # self.name = name

        # initialize the collection of items 
        self.items = ['pencil', 'car', 'herbs',
                      'pills', 'laptop', 'cigerrete',
                      'vodka', 'plane', 'pan', 'books',
                    ]
        
    
    def generate_items(self):
        """Return a list of 5 to 8 random items for each room """
        total_items = random.randint(5,8) # Pick a random number from 5 to 8
        room_items = []

        for item in range(0, total_items):
            # pick the random items from the list and store it to room items list
            room_items.append(self.items[random.randint(0, len(self.items)-1)]) 

        
        return room_items



# A player can enter a room from any of the compass directions
class Room:

    def __init__(self, name='Unknown', items = None, north = None, east = None, south = None, west = None):
    # Give each room a sensible name
        self.name = name
        self.items = items
 
    # Setup other rooms the player can enter
        self.north = north
        self.east = east
        self.south = south
        self.west = west
    
    # Display the list of items in the room
    def show_items(self):
        # time complexity O(n**2)
        for i in range(0, len(self.items)):
            print("%d.%s"%(i+1, self.items[i]))
            
# Represents the current player
class Player:
    def __init__(self, name='Unknown'):
        self.name = name
        self.items = []

    def show_picked_items(self):
        """Show all the collected items """
        # time Complexity : O(n**2)
        print("Name: " + self.name.title())
        print("*"*30)
        print("Total Items: %d")

        # Make a non repeted list 
        non_repeat_items = []
        for item in self.items:
            if item not in non_repeat_items:
                # assign all the unique items to non_repeat_items list 
                non_repeat_items.append(item)

        # show the picked_item name with quantity 
        for item in non_repeat_items:
            print("%s = %d"%(item,self.items.count(item)))
 
# Overall game code and logic 
class Game:

    def __init__(self, startRoom):
        self.start = startRoom
 
    def play(self, player):
        self.player = player



# Add game play code here
# Setup the game board rooms can be defined here and as well as the player name. Your code should start from here without modifying the above section. 
# Define a (3X5) 2D array for easily move from one room to another beased on a compass direction(N,E,W,S)

room_map = []
count = 1
total_items = 0
for i in range(3):
    rooms = []
    for j in range(5):
        items = Item().generate_items() #Generate random list of items for each room
        name = "Room - " + str(count) # Generate room names sequntually 
        room = Room(name, items) 
        count += 1
        # Store all the room objects into a 'room_map' list to use 
        # it later when player picked items from the room and navigate each room
        rooms.append(room) 
        total_items += len(items)
    room_map.append(rooms)

def show_room_maps():
    print("""
            *******************************
            * R1  * R2  * R3  * R4  * R5  *
            *******************************
            * R6  *  R7 *  R8 *  R9 * R10 *
            *******************************
            * R11 * R12 * R13 * R14 * R15 *
            *******************************
    """)


def update_position(room_number):
    # to easily identify the room number using row-column beased layout
    # let say if room number is 15 then this function return room_key(row)= 2 and room_number(column) = 5
    if room_number <= 5:
        room_key = 0
    elif room_number <=10:
        room_key = 1
        room_number -= 5
    elif room_number <=15:
        room_key = 2
        room_number -= 10
    
    return [room_key,room_number]


# Get the player name from user
p = Player(input("Player Name: "))

while True:
    # main menu
    print("Hi, " + p.name.title())
    print("1.Show Rooms Map")
    print("2.Enter the Room")
    print("3.Exit")

    try:
        option = int(input("Select Option: "))
    except ValueError:
        print("Please select the valid items")
        continue

    if option == 1:
        # Show the rooms map 
        show_room_maps()
        hold = input("Press any key to back")
    elif option == 3:
        # Exit the game
        exit()
    elif option == 2:

        os.system("cls")
        # Initial position of the player in the room

        r = int(input("Enter the room number(1-15): "))
        temp = update_position(r)
        room_key = temp[0]
        room_number = temp[1]-1 # room number count from 0(row-column beased) in the room_object list

        while True:

            os.system("cls")
            print("You are in " + room_map[room_key][room_number].name)
            print("1.View items")
            print("2.Pick items")
            print("3.Go to another room using compass direction(N,E,S,W)")
            print("4.Rooms Direction")
            print("5.Main Menu")
            try:
                option = int(input("Select Option: "))
            except ValueError:
                print("Please select the valid items")
                continue

            if option == 1:
                # show the room items from selected room object
                os.system("cls") 
                print(room_map[room_key][room_number].name) # show the name of the room using room_key(row) and room_number_value(col)
                if len(room_map[room_key][room_number].items) == 0:
                    print("No more items available.")
                else:
                    room_map[room_key][room_number].show_items()

                a = input("Enter any key to go back")
                # clear the terminal 
                os.system("cls")   
            
            elif option == 2:
                while True:
                    os.system("cls")
                    # Game over condition 
                    # if all the items is picked then it will same number as the total items numbers in all room before picked any items
                    if total_items == len(p.items):
                        # show all the items 
                        p.show_picked_items() 
                        game_over = True
                        break

                    # check if no items available in the room 
                    if len(room_map[room_key][room_number].items) == 0:
                        print("No more items available.")
                        a = input("press any key to back to the previous menu")
                        break
                    else:
                        print(room_map[room_key][room_number].name + ": Available items\n")
                        room_map[room_key][room_number].show_items()
                        print("\nPick the items by number. enter 0 to finish")    
                        try:
                            option = int(input("Select item: "))
                        except ValueError:
                            print("Please select the valid items")
                            continue
                        if option == 0:
                            break
                        elif option > len(room_map[room_key][room_number].items):
                            print("Please select the valid numbers.")
                        else:
                            # Remove the picked item from the room and store it to the player picked item
                            picked_item = room_map[room_key][room_number].items[option-1]
                            room_map[room_key][room_number].items.pop(option-1) # Remove the picked items from room items 
                            p.items.append(picked_item) # add the picked items into player items list
                        

            elif option == 3:
                # Move to compas direction
                # Room Navigation using direction indicator(N,E,S,W)
                os.system("cls")
                while True:
                    print("You are in " + room_map[room_key][room_number].name)
                    nav = input("Move to next room Direction(N,E,S,W): ").lower() #N,E,S,W indicate North, East, South, West
                    flag = False # for no available in perticular direction
                    if nav=='n' and room_key > 0 :
                        # move to 1 row North side
                        room_key -= 1 
                        flag = True
                    elif nav=='s' and room_key < 2:
                        # move to 1 row South side
                        room_key += 1
                        flag = True
                    elif nav=='w':
                        # boudary column 
                        if room_number == 0 or room_number == 5 or room_number == 10:
                            flag = False 
                        else:
                            # move to 1 column west side
                            room_number -= 1
                            flag = True
                    elif nav=='e':
                        if room_number == 4 or room_number == 9 or room_number == 14:
                            flag = False 
                        elif room_number < 14:
                            # move to 1 column east side
                            room_number += 1
                            flag = True

                    if flag:
                        os.system("cls")
                        print("You are in " + room_map[room_key][room_number].name)
                        print("1.Continue moving") # Continue to move direction
                        print("2.Room items menu") #Room
            
                        try:
                            a = int(input("Select: "))
                            if a==2:
                                break
                            if a!=1:
                                print("Please Select the valid number")
                                break
                        except ValueError:
                            print("Please Select the valid number")
                            break



                    else:
                        print("No Room available at this direction.")
            
            elif option == 4:
                os.system("cls")
                print("You are in " + room_map[room_key][room_number].name)
                target_room = int(input("Which room you want to go: "))
                
                # get the terget rooms rows and columns number
                temp = update_position(target_room)
                target_room_key = temp[0]
                target_room_number = temp[1]

                # find the distance between current room (row, col) and target_room(rows , col)
                route_key = room_key - target_room_key
                route_number = room_number - target_room_number 


                # to hold the path all beasd on current room and target room distance 
                path = ""
                
                # calculate the final route keys 
                if route_key > 0:
                    # if the cureent and current key distance is positive then it'll go to North side
                    path += "North, " * route_key
                elif route_key < 0:
                    # if the cureent and current key distance is negative then it'll go to South side
                    route_key = -route_key # to make it positive for multiply
                    path += "South, " * route_key
                else:
                    path +='' #current key and target key deifferance is Zero than it mean it's the same room 


                if route_number > 0:
                    # if the cureent and current room number distance is positive then it'll go to West side 
                    path += 'West, ' * route_number
                elif route_number < 0:
                    # if the cureent and current room number distance is negative then it'll go to East side
                    route_number = -route_number
                    path += 'East, ' * route_number
                else:
                    #current room number and target room number deifferance is Zero than it mean it's the same room 
                    path += ''
    
                print("Your Path is: " + path)
                a = input("\nEnter any key to back")

            elif option == 5:
                # Go to the main menu
                os.system("cls")  
                break 

            

    else:
        print("Please Select the valid numbers")

    os.system("cls")
