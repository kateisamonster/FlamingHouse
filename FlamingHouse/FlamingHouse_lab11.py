#Flaming House
#Team 7 Kate Adler, Michael Garber, Michael Lee      
import time
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

balcony = {"message": "Finally, a breath of fresh air.  You know you can't jump from here.  Oh look!  It's Mr. Peanut Butter!  You found him!",
           "access":"extinguisher"}

outside = {"message": "outside now"} #TODO: fix win condition

fHouse = {"bedroom" : bedroom, "closet" : closet,  "livingroom" : livingroom, "kitchen" :kitchen, "bathroom" :  bathroom, "diningroom" : diningroom, "balcony" : balcony, "outside" : outside}

#move = 0, action = 1, item = 2.  Format: message, index, key
gtBed = ("Go to Bedroom",0,"bedroom")
gtCloset = ("Go to Closet",0,"closet")
gtLiving = ("Go to Living Room",0,"livingroom")
gtKitchen = ("Go to Kitchen",0,"kitchen")
gtBath = ("Go to Bathroom",0,"bathroom")
gtDining = ("Go to Dining Room",0,"diningroom")
gtBalcony = ("Go to Balcony",0,"balcony")
gtOutside = ("Go Outside",0,"outside")
atScream = ("Scream for help",1,"HEYYYYY ANYONE OUT THERE?\nNo one can hear you...")

#Choices
bedroom["choices"] = {1 : gtBath, 2 : gtCloset, 3 : gtDining}
closet["choices"] = {1: gtBed}
livingroom["choices"] = {1 : gtKitchen, 2 : gtDining, 3 : gtBalcony}
kitchen["choices"] = {1 : gtDining, 2 : gtLiving}
bathroom["choices"] = {1 : gtBed}
diningroom["choices"] = {1 : gtLiving, 2 : gtKitchen , 3 : gtBed}
balcony["choices"] = {1 : gtLiving, 2 : atScream}

#==========================================================#
#main
#==========================================================#
def main():
    #Welcome Message
    currentRoom = "bedroom"
    print(welcome)
    choice = str(raw_input("Please enter a command:")).lower().rstrip()
    if choice != "start":
        print("Goodbye!")
    else:
        displayCurrentRoom(currentRoom)
        while choice != "exit":
            #print("what is the current room:", currentRoom)
            choice = raw_input("Please enter a command: ").lower().rstrip()
            currentRoom = choices(choice,currentRoom)

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
    #print( choicesDict)
    if choice == "help":
        displayHelp()
    # elif choice == "inventory":
    #     displayCurrentInventory()
    #     #choice not included
        return room
    elif choice == "exit":
        exit()
    elif choice not in keyChoices:
        print("Not an available Choice")
        displayCurrentRoom(room)
        return room
    else:
        #print("Choice FOUND")
        #choicesDict = fHouse[currentRoom]["choices"]
        act = choicesDict[choice][1]
        val = choicesDict[choice][2]
        #print("act : %s\t val : %s"%(act,val))
        #moving
        if act == 0:
            currentRoom = val
            print("=" * 50)	
            print "Current Room",currentRoom
            displayCurrentRoom(val)
            #print("ChoicesDict",choicesDict[2])
            return currentRoom
        elif act ==1:
            print val
            time.sleep(2)
            displayCurrentRoom(room)
            return room

#==========================================================#
#Functions
#==========================================================#
#Display room message
def displayCurrentRoom(room):
    print("=" * 50)	
    #print "Display current room: ",room
    print(fHouse[room]["message"])
    displayCurrentChoice(room)
#Display Choices
def displayCurrentChoice(room):
    for key, item  in fHouse[room]["choices"].items():
        print("%s : %s"%(key, item[0]))
#Display help
def displayHelp():
    print(welcome) #TODO: add help text

# def addToInventory(item):
#     inventory[item] = True

# def removeFromInventory(item):
#     inventory[item] = False

# def moveToRoom(desiredRoom):
#     currentRoom = desiredRoom
#     print(currentRoom)
#     displayCurrentRoom()

# def displayCurrentInventory():
#     for key, value in fHouse[room].items():
#         print(value)





if __name__ == "__main__":
    main()
