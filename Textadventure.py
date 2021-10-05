# some command stuff
badInput = "Sorry, please enter a valid command and try again."
userHelper = "Here are the commands currently available: look, take [object], leave (currently ends the game), wcidh"
GameOver = False
homeBedroomMoneyThere = True
homeWalkingStickThere = True
homeBedroomSlingshotThere = True
homeBedroomAmmoThere = True

'''
-To do:
        -make house
        -draw out map on some other software
        -organise the items
        -plan out the starting city
                -create map
        -make "use" function
                -make "use" function
                -make error message for "use" function
                -make "use" function for several items
        -make adders and subtracters for treasure, ammo, and HP
                -adders
                        -HP
                -subtracters
                        -treasure
                        -ammo
                        -hp
                                -currenthp
                                -maxhp
        -make a levelling system
        -make a combat system
                -make encounters
                        -random
                        -choreographed
'''
class CombatSystem:
        class Enemies:
                class EnemySlot1:
                        Enemy1HP = None
                        Enemy1Attack = None
class locations:
        class Agathor:
                class AgathorWest:
                        class Home:
                                class HomeUpstairs:
                                        class homeBedroom:
                                                while(CurrentRoom == "HomeBedroom"):
                                                        Input1 = input('What would you like to do?')
                                                        if Input1 == "look":
                                                        print("There is a small purse filled with 100 coins on the table next to your bed, and above that is a walking stick and slingshot, with a pouch full of 100 pellets sitting beside it. At the far end of the room is the door.")
                                                        elif Input1 == "take slingshot" and homeBedroomSlingshotThere == True:
                                                                print("Slingshot taken.")
                                                                Bow = Slingshot
                                                                homeBedroomSlingshotThere = False
                                                        elif Input1 == "take pellets" and homeBedroomAmmoThere == True:
                                                                print("pellets taken.")
                                                                AmmoAdder2 = 100
                                                                AmmoAdder()
                                                                homeBedroomAmmoThere = False
                                                        elif Input1 == "take coins" and homeBedroomMoneyThere == True:
                                                                TemporaryTreasure2 = 100
                                                                TreasureAdder()
                                                                homeBedroomMoneyThere = False
                                                        elif Input1 == "leave":
                                                                CurrentRoom = "HomeMainArea"
                                                                break
                                                        elif Input1 == "help":
                                                                print(userHelper)
                                                        else:
                                                                print(badInput)
                                class HomeItems:
                                        homeBedroomMoneyThere = True
                                        homeWalkingStickThere = True
                                        homeBedroomSlingshotThere = True
                                        homeBedroomAmmoThere = True
                                        class homeBedroom:



















CurrentRoom = "HomeBedroom"
class Inventory:
        InventorySlot1 = None
        InventorySlot2 = None
        InventorySlot3 = None
        InventorySlot4 = None
        InventorySlot5 = None
        InventorySlot6 = None
        InventorySlot7 = None
        InventorySlot8 = None
        InventorySlot9 = None
        InventorySlot10 = None
        Treasure = None
        HP = 100
        MaxHP = 100
        XP = 0
        Sword = None
        Bow = None
        Ammo = 0
        Stick = 1
        Slingshot = 1
print("You have woken up. It is time to go.")
Ammo = 0
AmmoAdder1 = 0
#define AA2 as the number you want to add to total
AmmoAdder2 = 0
def AmmoAdder():
        AmmoAdder1 = Ammo
        Ammo = 0
        Ammo = AmmoAdder2 + AmmoAdder1
        AmmoAdder1 = 0
        AmmoAdder2 = 0
TemporaryTreasure1 = 0
#define TT2 as the number you want to add to the total
TemporaryTreasure2 = 0
def TreasureAdder():
        TreasureAdder1 = Treasure
        Treasure = None
        Treasure = TreasureAdder2 + TreasureAdder1
        TreasureAdder1 = 0
        TreasureAdder2 = 0
	




while(CurrentRoom == "HomeBedroom"):
        Input1 = input('What would you like to do?')
        if Input1 == "look":
                print("There is a small purse filled with 100 coins on the table next to your bed, and above that is a walking stick and slingshot, with a pouch full of 100 pellets sitting beside it. At the far end of the room is the door.")
        elif Input1 == "take slingshot" and homeBedroomSlingshotThere == True:
                print("Slingshot taken.")
                Bow = Slingshot
                homeBedroomSlingshotThere = False
        elif Input1 == "take pellets" and homeBedroomAmmoThere == True:
                print("pellets taken.")
                TemporaryAmmo2 = 100
                AmmoAdder()
                homeBedroomAmmoThere = False
        elif Input1 == "take coins" and homeBedroomMoneyThere == True:
                TemporaryTreasure2 = 100
                TreasureAdder()
                homeBedroomMoneyThere = False
        elif Input1 == "leave":
                CurrentRoom = "HomeMainArea"
                break
        elif Input1 == "help":
                print(userHelper)
        else:
                print(badInput)
while(CurrentRoom == "HomeMainArea"):
        HomeInput == input('What would you like to do?')
        if HomeInput == "look":
                print("You are in the main floor of your house. On this floor is a storeroom for food, a kitchen, and a table, on which sits a note. Here are some things you can do: 'read note', 'enter pantry', 'enter kitchen', 'go downstairs', 'exit house'")
        elif HomeInput == "enter pantry":
                print('You are in a pantry')
