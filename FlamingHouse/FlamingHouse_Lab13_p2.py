#Flaming House
#Team 7 Kate Adler, Michael Garber, Michael Lee      
import time
import os
#==========================================================#
#Initialize Room variables here
#==========================================================#
welcome = ("Welcome to the FireHouse! \n"
    "The objective of the game is to escape the house before you die.\n"
    "If you would like to start, type 'start' and press ENTER\n"
    "If you would like help, type 'help' and press ENTER\n"
    "Type 'exit' and press ENTER at any time to end the game\n")

bedroom = {"message" : "You wake up in a room dark filled with smoke.  The smoke detector alarm is blaring in your ears, and you cannot hear much", 
           "access":"universal_access"}

closet = {"message": "Your closet is extremely small and you cannot see anything.",
          "access":"universal_access"}

livingroom = {"message":"You see your Large television in front of your small coach.  You hear the whimperings of a frightened dog.  The drapes are on fire.",
              "access":"key"}

kitchen = {"message":"You see a small kitchen",
           "access":"universal_access"}

bathroom = {"message":"Your bathroom is extremely dirty.  You see a lot of dirty clothes on the floor",
            "access":"universal_access"}

diningroom = {"message": "Your dining room is very small",
              "access":"universal_access"}

balcony = {"message": "Finally, a breath of fresh air.  You know you can't jump from here.  Oh look!  It's Dr. Cheetoes!  You found him!",
           "access":"extinguisher"}

outside = {"message": "outside now", "access" : "towel"} #TODO: fix win condition

fHouse = {"bedroom" : bedroom, "closet" : closet,  "livingroom" : livingroom, "kitchen" :kitchen, "bathroom" :  bathroom, "diningroom" : diningroom, "balcony" : balcony, "outside" : outside}

#move = 0, action = 1, item = 2.  Format: message, index, key
#move rooms
gtBed = ("Go to Bedroom",0,"bedroom")
gtCloset = ("Go to Closet",0,"closet")
gtLiving = ("Go to Living Room",0,"livingroom")
gtKitchen = ("Go to Kitchen",0,"kitchen")
gtBath = ("Go to Bathroom",0,"bathroom")
gtDining = ("Go to Dining Room",0,"diningroom")
gtBalcony = ("Go to Balcony",0,"balcony")
gtOutside = ("Go Outside",0,"outside")
#actions
actScream = ("Scream for help",1,"HEYYYYY ANYONE OUT THERE?\nNo one can hear you...")
actSitDown = ("Sit down on the Chair",1,"You sat down on the chair")
actCabinet = ("Open the cabinet",1,"There is nothing in there")

#inventory
inPhone = ("Grab your Phone",2,"phone")
inExtinguisher = ("Grab a Fire Extinguisher",2,"extinguisher")
inWetTowel = ("Grab the wet towel in the sink",2, "towel")
inDog = ("Grab the dog",2,"dog")
#Useless Items
inWater = ("Grab the water bottle on the counter",2,"bottle")
inBlanket = ("Grab the blanket in the closet",2,"blanket")


#Choices
bedroom["choices"] = {1 : gtBath, 2 : gtCloset, 3 : gtDining, 4 : inPhone}
closet["choices"] = {1: gtBed, 2 : inBlanket}
livingroom["choices"] = {1 : gtKitchen, 2 : gtDining, 3 : gtBalcony,  4 : gtOutside, 5 : inWater}
kitchen["choices"] = {1 : gtDining, 2 : gtLiving, 3 : inExtinguisher}
bathroom["choices"] = {1 : gtBed, 2 : inWetTowel, 3 : actCabinet}
diningroom["choices"] = {1 : gtLiving, 2 : gtKitchen , 3 : gtBed, 4 : actSitDown}
balcony["choices"] = {1 : gtLiving, 2 : actScream, 3 : inDog}

#Global Variables
inventory = []

#==========================================================#
#main
#==========================================================#
def main():
    #Welcome Message
    currentRoom = "bedroom"
    name = str(raw_input("Please enter your name: ")).rstrip()
    printNow(welcome)
    choice = str(raw_input("Please enter a command:")).lower().rstrip()
    if choice != "start":
        printNow("Goodbye!")
    else:
        displayCurrentRoom(currentRoom)
        moveCounter = 0
        MAX_MOVE = 20
        while choice != "exit" and moveCounter < MAX_MOVE and currentRoom != "outside":
            #printNow("CURRENT ROOM RIGHT MEOW: " + currentRoom)
            choice = raw_input("Please enter an index: ").lower().rstrip() 
            if choice == "help":
                printNow ("HELP")
                displayHelp()
            elif choice == "exit":
                os._exit(1)
            elif choice == "inventory":
                for item in inventory:
                    printNow (item)
            else:
                moveCounter+=1
                #if choice in (fHouse[currentRoom]["choices"][3]):
                currentRoom = choices(choice,currentRoom)
                #printNow("CURRENT ROOM AFTER CHOICES"+currentRoom)
            if currentRoom == "outside":
              time.sleep(2)
              break
        #WIN OR LOSE
        if moveCounter < MAX_MOVE:
            if "dog" in inventory:
                displayDogWin(name)
            else:
                displayWin(name)
        else:
            displayLose(name)
        printNow( "The program will exit in ")
        for i in range (3, 1, -1):
            printNow(i)
            time.sleep(1)
        os._exit(1)

def displayDogWin(name):
    showInformation("You are a HERO %s have done Dr. Cheetoes a great service by escorting him and his faithful servant from the raging infero."%(name))

def displayWin(name):
    showInformation( "You have exited the building.  %s... You left your dog, but you are alive.  Poor Dr. Cheetos..."%(name))
    
def displayLose():
    showInformation ("YOU DIED.  You have lost the game.")
            
#==========================================================#
#Choices
#==========================================================#
def choices(choice,room):
    choicesDict = fHouse[room]["choices"]
    keyChoices = []

    try:
        choice = int(choice)
    except:
        choice = str(choice)    
    for key in choicesDict:
        keyChoices.append(key)
    #printNow( choicesDict)

    if choice not in keyChoices:
        printNow("Not an available Choice")
        displayCurrentRoom(room)
        return room
    else:
        #printNow("Choice FOUND")
        #choicesDict = fHouse[currentRoom]["choices"]
        act = choicesDict[choice][1]
        val = choicesDict[choice][2]
        #printNow("act : %s\t val : %s"%(act,val))
        #moving

        #moveRoom
        if act == 0:
            return moveRoom(val,room)
        #doAction
        elif act == 1:
            return doAction(val,room)
        #doInventory
        elif act == 2:
            return doInventory(val,room)

def moveRoom(val,room):
    nextRoom = val
    if val == "balcony":
        #check to see if extinguisher is in inventory
        if "extinguisher" not in inventory:
            printNow ("You need something to put out the fire")
            displayCurrentRoom(room)
            return room
        else:
          printNow ("You use the fire extinguisher to put out the flames on the drapes and exit to the balcony.")
          displayCurrentRoom(nextRoom)
          return nextRoom
    elif val == "outside":
        #Check to see if towel is in inventory
        if "towel" not in inventory:
            printNow ("The door is too hot to open. Find something to protect your hands.")
            displayCurrentRoom(room)
            return room
        else:
            printNow ("You exit the house, using the towel to protect your hand from the hot doorknob.")
			#displayCurrentRoom(nextRoom)        
            return "outside"
    #Move to next room
    else:
        printNow("=" * 50)	
        printNow ("Current Room: " + nextRoom)
        displayCurrentRoom(val)
        return nextRoom

def doAction(val,room):
    printNow( val)
    time.sleep(2)
    displayCurrentRoom(room)
    return room

def doInventory(val, room):
    printNow("=" * 50)	
    if val in inventory:
        printNow ("You already have picked up %s"%(val))
        printNow("=" * 50)	
    else:
        inventory.append(val)
        printNow ("You have grabbed %s.  You will find it in your inventory"%(val))
        printNow("=" * 50)	
        displayCurrentRoom(room)
    return room

#==========================================================#
#Functions
#==========================================================#
#Display room message
def displayCurrentRoom(room):
    printNow("=" * 50)	
    #printNow "Display current room: ",room
    printNow(fHouse[room]["message"])
    displayCurrentChoice(room)
#Display Choices
def displayCurrentChoice(room):
    for key, item  in fHouse[room]["choices"].items():
        printNow("%s : %s"%(key, item[0]))
#Display help
#def displayHelp()
#         printNow(value)

main()
