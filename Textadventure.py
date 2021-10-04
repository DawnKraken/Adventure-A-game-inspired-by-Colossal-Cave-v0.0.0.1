# some command stuff
badInput = "Sorry, please enter a valid command and try again."


























CurrentRoom = "Home"
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
while(CurrentRoom == "Home"):
	HomeInput = input('What would you like to do?')
	if HomeInput == "look":
		print("There is a pouch filled with 50 coins on the table next to your bed, and above that is a walking stick and slingshot, with a pouch full of 100 pellets next to it.")
	elif HomeInput == "take stick":
		Sword = Stick
	elif HomeInput == "take slingshot":
		Bow = Slingshot
		Ammo = Ammo + 100
	elif HomeInput == "leave":
		break
	else:
		print(badInput)
