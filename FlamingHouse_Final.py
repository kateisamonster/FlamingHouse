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
    "Once the game is underway you can type 'help' and press ENTER for assistance\n"
   "Type 'exit' and press ENTER at any time to end the game\n")

bedroom = {"message" : "You wake up in a room dark filled with smoke.  The smoke detector alarm is blaring in your ears, and you cannot hear much", 
           "pic":"bedroom.jpg", 
           "is_first_time":True}

closet = {"message": "Your closet is extremely small and you cannot see anything.",
          "pic":"closet.jpg", 
          "is_first_time":True}

livingroom = {"message":"You see your Large television in front of your small coach.  You hear the whimperings of a frightened dog.  The drapes are on fire.",
              "pic":"livingroom.jpg", 
              "is_first_time":True}

kitchen = {"message":"You see a small kitchen",
           "pic":"kitchen.jpg", 
           "is_first_time":True}

bathroom = {"message":"Your bathroom is extremely dirty.  You see a lot of dirty clothes on the floor",
            "pic":"bathroom.jpg", 
            "is_first_time":True}

diningroom = {"message": "Your dining room is very small",
              "pic":"diningroom.jpg", 
              "is_first_time":True}

balcony = {"message": "Finally, a breath of fresh air.  You know you can't jump from here.  Oh look!  It's Dr. Cheetoes!  You found him!",
           "pic" : "balcony.jpg", 
           "is_first_time":True}

outside = {"message": "outside now", 
            "is_first_time":True} #TODO: fix win condition

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

inventory = []

#==========================================================#
#main
#==========================================================#
def main():
    printNow("Please select the folder where this game is located on your hard drive.")
    setMediaPath()
    #Welcome Message
    fireSound = makeSound("fire.wav")
    play(fireSound)
    currentRoom = "bedroom"
    #Get Name input
    name = str(raw_input("Please enter your name: ")).rstrip()
    printNow(welcome)
    choice = str(raw_input("Please enter a command:")).lower().rstrip()
    if choice != "start":
        printNow("Goodbye!")
    #START THE GAME
    else:
        #Display current room before while statement
        displayCurrentRoom(currentRoom)
        moveCounter = 0
        MAX_MOVE = 20
        #While loop until the game ends (lose or win)
        while choice != "exit" and moveCounter < MAX_MOVE and currentRoom != "outside":
            choice = raw_input("Please enter an index: ").lower().rstrip()
            time.sleep(.5)
            #Help Option here
            if choice == "help":
                printNow ("HELP")
                displayHelp()
            #Exit option here
            elif choice == "exit":
                os._exit(1)
            #Print out current inventory
            elif choice == "inventory":
                for item in inventory:
                    printNow (item)
            #If there is an action
            else:
                moveCounter+=1
                currentRoom = choices(choice,currentRoom)
                if fHouse[currentRoom]["is_first_time"]:
                    #if you have won the game, break
                    if currentRoom == 'outside':
                        break
                    #show picture of the room and make sure it doesn't display again.
                    else:
                        show(makePicture(fHouse[currentRoom]["pic"]))
                        fHouse[currentRoom]["is_first_time"] = False
            #if you have won the game, break (In case first one fails)            
            if currentRoom == "outside":
              break
            
        #WIN OR LOSE
        if moveCounter < MAX_MOVE:
            #Check if there is a dog or if there isnt
            if "dog" in inventory:
                displayDogWin(name)
            else:
                displayWin(name)
        #Display lose and play sound.
        else:
            displayLose()
        printNow( "The program will exit in ")
        #Exiting the game
        for i in range (3, 1, -1):
            printNow(i)
            time.sleep(1)
        os._exit(1)
            
#==========================================================#
#Choices
#==========================================================#
def choices(choice,room):
    choicesDict = fHouse[room]["choices"]
    keyChoices = []
    #Try catch for the input.  Make sure its a valid choice
    try:
        choice = int(choice)
    except:
        choice = str(choice)    
    for key in choicesDict:
        keyChoices.append(key)

    #If it is not a valid choice, tell the user
    if choice not in keyChoices:
        printNow("Not an available Choice")
        displayCurrentRoom(room)
        return room
    #If the choice is valid
    else:
        act = choicesDict[choice][1]
        val = choicesDict[choice][2]
        #moveRoom
        if act == 0:
            return moveRoom(val,room)
        #doAction
        elif act == 1:
            return doAction(val,room)
        #doInventory
        elif act == 2:
            return doInventory(val,room)
        
#==========================================================#
#Moving Rooms
#==========================================================#
#Move room function.  Check to see if the room is balcony or outside.
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
          play(makeSound("dog.wav"))
          return nextRoom
    elif val == "outside":
        #Check to see if towel is in inventory
        if "towel" not in inventory:
            printNow ("The door is too hot to open. Find something to protect your hands.")
            displayCurrentRoom(room)
            return room
        else:
            printNow ("You exit the house, using the towel to protect your hand from the hot doorknob.")     
            return "outside"
    #Move to next room
    else:
        printNow("=" * 50)	
        printNow ("Current Room: " + nextRoom)
        displayCurrentRoom(val)
        return nextRoom
    
#==========================================================#
#Functions
#==========================================================#
#Do action.  val is the value from the key that is extracted above
def doAction(val,room):
    printNow( val)
    time.sleep(2)
    displayCurrentRoom(room)
    return room

#Add item to inventory.  Check whether it is in the inventory or not.
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
#Display Functions
#==========================================================#
#Dog win function
def displayDogWin(name):
    show(makePicture('winpic.jpg'))
    play(makeSound("puppywin.wav"))
    showInformation("You are a HERO %s have done Dr. Cheetoes a great service by escorting him and his faithful servant from the raging infero."%(name))

#Without Dog win function
def displayWin(name):
    show(makePicture('regwin.jpg'))
    play(makeSound("mancry.wav"))
    showInformation( "You have exited the building.  %s... You left your dog, but you are alive.  Poor Dr. Cheetos..."%(name))

#Lose Function
def displayLose():
    play(makeSound("lose.wav"))
    showInformation ("YOU DIED.  You have lost the game.")

#Display the help
def displayHelp():
  showInformation(welcome)
  
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
def displayHelp():
    printNow(welcome)

main()
