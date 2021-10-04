# some command stuff
badInput = "Sorry, please enter a valid command and try again."
userHelper = "Here are some commands: take [object], look, trash, leave, north, n, east, e, south, s, west, w"
TemporaryTreasure1 = 0
#define TT2 as the number you want to add to the total
TemporaryTreasure2 = 0
def TreasureAdder():
        TemporaryTreasure1 = Treasure
        Treasure = None
        Treasure = TemporaryTreasure2 + TemporaryTreasure1
        TemporaryTreasure1 = 0
        TemporaryTreasure2 = 0
TemporaryAmmo1 = 0
#define TA2 as the number you want to add to total
TemporaryAmmo2 = 0
def AmmoAdder():
        TemporaryAmmo1 = Ammo
        Ammo = None
        Ammo = TemporaryAmmo2 + TemporaryAmmo1
        TemporaryAmmo1 = 0
        TemporaryAmmo2 = 0






















CurrentRoom = "HomeBedroom"
#inventory
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
#items
Treasure = None
Sword = None
Bow = None
Ammo = 0
Stick = 1
Slingshot = 1
print("You have woken up. It is time to go.")
homeBedroomMoneyThere = True
homeWalkingStickThere = True
homeBedroomSlingshotThere = True
homeBedroomAmmoThere = True
while(CurrentRoom == "HomeBedroom"):
        Input1 = input('What would you like to do?')
        if Input1 == "look":
                print("There is a pouch filled with 100 coins on the table next to your bed, and above that is a walking stick and slingshot, with a small purse full of 100 pellets next to it. At the far end of the room is the door.")
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
#while(CurrentRoom == "HomeMainArea"):
        #HomeInput == input('What would you like to do?')
        #if HomeInput
