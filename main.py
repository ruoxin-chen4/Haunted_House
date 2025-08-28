global mapCollected 
global keyOne
global keyTwo
global crowBar
global teddyBear
global flashlight
global batteries
global lockedBox
global pieceOfcheetos
global knife
global achievement
global RIDDLE
global CHEETOS
global ESCAPEHOUSE
global ESCAPE

# Variables
mapCollected = 0
keyOne = 0
keyTwo = 0
crowBar = 0
teddyBear = 0
flashlight = 0
batteries = 0
lockedBox = 0
pieceOfcheetos = 0
knife = 0
RIDDLE = 0
CHEETOS = 0
ESCAPE = 0
ESCAPEHOUSE = 0

# Define Slow Print
import sys,time
def sprint(str):
   for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(3./90) 

# GHOST SECTION

# List Achievement gained at the end
def Achievement():
	global RIDDLE
	global CHEETOS
	global ESCAPEHOUSE
	global ESCAPE
	sprint("\nCongratulations! You have escaped the Haunted House! Here are the \033[1;36;40machievements\033[0m that you have earned throughout the game!")
	if CHEETOS + RIDDLE + ESCAPEHOUSE + ESCAPE == 4:
		achievement = ["Dangerously CHEESY!", "Ghost's Riddle Solved!", "Haunted House Escaped!", "'Escapee! :D"]
		print(achievement)
	elif RIDDLE + ESCAPE + ESCAPEHOUSE == 3:
		achievement = ["Ghost's Riddle Solved!", "Haunted House Escaped!", "'Escapee! :D"]
		print(achievement)
	
# Riddle
def riddle():
	global RIDDLE
	global ESCAPEHOUSE
	sprint("\n\033[0;35mAlright I’ll let you go, on one condition, if you are able to answer this riddle correctly.\033[0m")
	sprint("\033[0;35mI have a tail and a head, but no body. What am I?\033[0m")
	while True:
		riddleAnswer = input()
		if riddleAnswer.lower() in ["A coin", "a coin", "coin", "Coin", "COIN"]:
			sprint("\n\033[0;35mGood job you are correct, you may now Leave.\n\n\033[1;36;40mACHIEVEMENT UNLOCKED:\033[0m")
			achievement = ["Ghost's Riddle Solved!"]
			print(achievement)
			RIDDLE = RIDDLE + 1
			sprint("\n\033[1;36;40mACHIEVEMENT UNLOCKED:\033[0m")
			achievement = ["Haunted House Escaped!"]
			print(achievement)
			ESCAPEHOUSE = ESCAPEHOUSE + 1
			Achievement()
			break
		else:
			sprint("\n\033[0;35mIncorrect, try again.\033[0m")
			RIDDLE = RIDDLE + 0
			ESCAPEHOUSE = ESCAPEHOUSE + 0
			continue

# Ghost Introduction
def ghost():
	sprint("\n\033[0;35mI haven’t had visitors in a while…… Who's there?\033[0m")
	name = input("\033[0;35mEnter your name: \033[0m")
	sprint("\n\033[0;35mHello, " + name + "...\033[0m")
	time.sleep(1)
	sprint("\n\033[0;35mDo you wish to enter through this door instead?\033[0m")
	answertoghost = input()
	if answertoghost in ["yes", "Yes", "yeah", "sure", "ok", "alr", "yup", "ye", "ya"]:
		sprint("\nYou enter through the \033[94mother door\033[0m but there is an emptiness that you've never seen before. You hear the \033[94mdoor\033[0m behind you close. A shrill voice echoes from the walls. You should have not trusted that \033[94mghost\033[0m.")
		time.sleep(1)
		sprint("\n\033[31mYOU DIED!\033[0m") 
	elif answertoghost in ["no", "No", "Nope", "nope", "nah", "nooo"]:
		sprint("\nYou stay with the \033[94mghost\033[0m and continue to answer their questions.")
		riddle()

#	MISSION FOUR SECTION
	
# Define Out Of The Room
def outside():
	global ESCAPE
	time.sleep(1)
	sprint("\n\033[1;36;40mAchievement Acquired:\033[0m")
	achievement = ["Escapee! :D"]
	print(achievement)
	ESCAPE = ESCAPE + 1
	sprint("\nBUT! There are \033[94mtwo doors\033[0m??\n- \033[32mWhich door would you go to? Left or right?\033[0m -")
	door = input()
	if door.lower() in ["Left", "left"]:
		sprint("\nThere’s nothing in this \033[94mdoor\033[0m…You walked in a few steps to see the full view of the room. *SLAM!… \033[31mThe door is locked! Unfortunately, you locked yourself in the room and this time, nothing can help you…\033[0m") 
	elif door.lower() in ["Right", "right"]:
		sprint("\nThis room is also dark… It leads to another floor.. The \033[94mdoor\033[0m closes itself as you step down the stairs. You looked back but see nothing. You got down and started looking around the room, then you saw a \033[94mwhite clear creature\033[0m standing by a \033[94mdoor\033[0m that is absolutely not a thing that a human can open. You walked up to the \033[94mcreature\033[0m and realized it could be a \033[94mghost\033[0m… You looked at the \033[94mghost\033[0m and the \033[94mghost\033[0m started speaking…")
		ghost()
	
# Break Door with Crowbar
def breakDoor():
	global crowBar
	if crowBar == 1:
		sprint("\nEven with the absolute filth there is on the \033[94mcrowbar\033[0m, you grab it and rush to the \033[94mlocked door\033[0m. You hook it onto the \033[94mchained door\033[0m and manage to miraculously break the metal off.\033[0m")
	outside()
		
# Define North (Mission Four)
def northThree():
	sprint("\nThe light of your \033[94mflashlight\033[0m reveals the same \033[94mshelf\033[0m you searched.\n- \033[34mSearch again?\033[0m -")
	comment = input()
	if comment.lower() in ["yes", "Yes", "yeah", "sure", "ok", "alr", "yup", "ye", "ya"]:
		sprint("\nNothing is there.")
	elif comment.lower() in ["no", "No", "Nope", "nope", "nah", "nooo"]:
		sprint("\nYou leave the shelf.")
		
# Define South (Mission Four)
def southTwo():
	global achievement
	global CHEETOS
	sprint("\nYou \033[92mwalk back to the table\033[0m, wondering if there is anything of use to help your situation.\n- \033[34mSearch the table?\033[0m -")
	comment2 = input()
	if comment2.lower() in ["yes", "Yes", "yeah", "sure", "ok", "alr", "yup", "ye", "ya"]:
		sprint("\nYou find \033[94ma piece of Cheetos\033[0m lodged into the crevice of the table.\n- \033[33mDo you wish to keep this in your inventory?\033[0m -")
		comment22 = input()
		if comment22.lower() in ["yes", "Yes", "yeah", "sure", "ok", "alr", "yup", "ye", "ya"]:
			sprint("\n\033[1;36;40mAchievement Acquired:\033[0m")
			achievement = ["Dangerously CHEESY!"]
			print(achievement)
			CHEETOS = CHEETOS + 1
		elif comment22.lower() in ["no", "No", "Nope", "nope", "nah", "nooo"]:
			sprint("\nYou leave the Cheeto in the crevice.")
			CHEETOS = CHEETOS + 0
			
# Define East (Mission Four)
def eastThree():
	sprint("\nYou walk \033[92meast\033[0m, hoping to find something of use. But it seems that the only thing here is an \033[94mold, beaten-up teddy bear\033[0m.\n- \033[33mDo you wish to keep this in your inventory?\033[0m -")
	teddyBear = input()
	if teddyBear.lower() in ["yes", "Yes", "yeah", "sure", "ok", "alr", "yup", "ye", "ya"]:
		sprint("\n\033[93m*Teddy Bear added to inventory!\033[0m")
	if teddyBear.lower() in ["no", "No", "Nope", "nope", "nah", "nooo"]:
		sprint("\nIt continues to sit in the darkness for who knows how much longer.")
	
# Define West (Mission Four)
def westThree():
	global crowBar
	sprint("\nWalking \033[92mwest\033[0m, you find yourself in a pickle (not literally), there’s nothing but dust all around what seems to be a long, heavy tool. You turn on your flashlight and you realize it’s a \033[94mcrowbar\033[0m.\n- \033[33mDo you wish to keep this in your inventory?\033[0m -")
	crowbar = input()
	if crowbar.lower() in ["yes", "Yes", "yeah", "sure", "ok", "alr", "yup", "ye", "ya"]: 
		sprint("\n\033[93m*Crowbar added to inventory!\033[0m")
		crowBar = crowBar + 1
	if crowbar.lower () in ["no", "No", "Nope", "nope", "nah","nooo"]:
		sprint("\nYou leave it in the dust.")
	
# Define Mission Four
def missionFour():
	time.sleep(1)
	sprint("\n\033[36mMISSION FOUR: find the crowbar to open the chained door to get out\033[0m")
	time.sleep(1)
	while True:
		sprint("\n- \033[32mWhich direction will you choose: North, South, East, West, or Next?\033[0m -")
		path = input()
		if path.lower() in ["North", "north"]:
			northThree()
			continue
		elif path.lower() in ["South", "south"]:
			southTwo()
			continue 
		elif path.lower() in ["East", "east"]:
			eastThree()
			continue
		elif path.lower() in ["west", "West"]:
			westThree()
			continue
		elif path.lower() in ["next", "Next", "n", "N"]:
			breakDoor()
			break
		else:
			sprint("\n\033[31mYou can't walk in that direction.\033[0m")
			continue
		
# MISSION THREE SECION

# Check Map Pieces
def mapPieces():
	global mapCollected 
	if mapCollected == 4:
		sprint("\nAfter piecing the \033[94mmap\033[0m together, you realize the paper in front of you is displaying the structure of what seems to be the house you are in. According to the \033[94mmap\033[0m, you’re situated in the only room on the very top floor.")
		missionFour()
	if mapCollected != 4:
		sprint("\n\033[31mYou didn't find all the map pieces. Click Run to restart the game if you wish.\033[0m")
			
# Redfine West (Mission Three)
def westTwo2():
	global mapCollected 
	sprint("\n- \033[32mGo to the west?\033[0m -")
	west2 = input()
	if west2 in ["yes", "Yes", "yeah", "sure", "ok", "alr", "yup", "ye", "ya"]:
		sprint("\nIt’s the \033[94mshelf\033[0m again.\n- \033[34mUse the key on the locked box?\033[0m -")
		box2 = input()
		if box2.lower() in ["yes", "Yes", "yeah", "sure", "ok", "alr", "yup", "ye", "ya"]:
			sprint("\nThe \033[94mlocked box\033[0m opened. Many papers were stuffed inside the box. You flipped through the papers and found \033[94ma piece of the map\033[0m.\n- \033[33mKeep it in the inventory?\033[0m -")
			map2 = input()
			if map2.lower() in ["yes", "Yes", "yeah", "sure", "ok", "alr", "yup", "ye", "ya"]:
				sprint("\n\033[93m*Map piece added to inventory!\033[0m")
				mapCollected = mapCollected + 1
				mapPieces()
			elif map2.lower() in ["no", "No", "Nope", "nope", "nah", "nooo"]:
				sprint("\nMap piece left in box.")
				mapCollected = mapCollected + 0
				mapPieces()
		elif box2.lower() in ["no", "No", "Nope", "nope", "nah", "nooo"]:
			sprint("\nThe box has been left alone.")
			mapPieces()
	elif west2 in ["no", "No", "Nope", "nope", "nah", "nooo"]:
		mapPieces()
			
# Redefine South (Mission Three)
def southeastTwo2():
	sprint("\nIt’s the \033[94mbed\033[0m again.\n- \033[34mWhere do you want to search? Top or Under?\033[0m -")
	bedLocation = input()
	if bedLocation.lower() in ["bottom", "under","below"]:
		sprint("\nYou found a \033[94mkey\033[0m. Where do you think you could use this key?\n- \033[33mKeep this in your inventory?\033[0m -")
		key2 = input()
		if key2.lower() in ["yes", "Yes", "yeah", "sure", "ok", "alr", "yup", "ye", "ya"]:
			keyTwo + 1
			sprint("\n\033[93m*Added key to inventory!\033[0m")
			westTwo2()
		elif key2.lower() in ["no", "No", "Nope", "nope", "nah", "nooo"]:
			keyTwo + 0
			sprint("\n\033[31mYou decided to sit and wait till your death...\033[0m")
	elif bedLocation.lower() in ["top", "Top"]:
		sprint("\nThere's nothing here except a \033[94mpillow\033[0m.\n- \033[33mKeep this in your inventory?\033[0m -")
		pillow = input()
		if pillow.lower() in ["yes", "Yes", "yeah", "sure", "ok", "alr", "yup", "ye", "ya"]:
			sprint("\n\033[93m*Added Pillow to inventory!\033[0m")
			sprint("\n\033[31mYou have been here twice and did not find the needed item to escape. Please try again if you wish.")
		elif pillow.lower() in ["no", "No", "Nope", "nope", "nah", "nooo"]:
			sprint("\nPillow has been left on top of the bed.")
			sprint("\n\033[31mYou have been here twice and did not find the needed item to escape. Please try again if you wish.")
			
# Define West Two Point One (Mission Three)
def westTwopointOne():
	sprint("\n- \033[32mGo to the west?\033[0m -")
	west2pointOne = input()
	if west2pointOne in ["yes", "Yes", "yeah", "sure", "ok", "alr", "yup", "ye", "ya"]:
		sprint("\nIt’s the \033[94mshelf\033[0m again...But you don't have the \033[94mkey\033[0m to use on the \033[94mlocked box\033[0m.")
		sprint("- \033[32mGo back?\033[0m -")
		think = input()
		if think in ["yes", "Yes", "yeah", "sure", "ok", "alr", "yup", "ye", "ya"]:
			southeastTwo2()
		if think in ["no", "No", "Nope", "nope", "nah", "nooo"]:
			sprint("\n\033[31mThen you're stuck in this bulding forever...You have to go back.\033[0m")
			southeastTwo2()
	elif west2pointOne in ["no", "No", "Nope", "nope", "nah", "nooo"]:
		sprint("\nThen you better go back and search for that \033[94mKEY\033[0m.")
		southeastTwo2()
			
# Define West (Mission Three)
def westTwo():
	global mapCollected 
	sprint("\n- \033[32mGo to the west?\033[0m -")
	west2 = input()
	if west2 in ["yes", "Yes", "yeah", "sure", "ok", "alr", "yup", "ye", "ya"]:
		sprint("\nIt’s the \033[94mshelf\033[0m again.\n- \033[34mUse the key on the locked box?\033[0m -")
		box2 = input()
		if box2.lower() in ["yes", "Yes", "yeah", "sure", "ok", "alr", "yup", "ye", "ya"]:
			sprint("\nThe \033[94mlocked box\033[0m opened. Many papers were stuffed inside the box. You flipped through the papers and found \033[94ma piece of the map\033[0m.\n- \033[33mKeep it in the inventory?\033[0m -")
			map2 = input()
			if map2.lower() in ["yes", "Yes", "yeah", "sure", "ok", "alr", "yup", "ye", "ya"]:
				sprint("\n\033[93m*Map piece added to inventory!\033[0m")
				mapCollected = mapCollected + 1
				mapPieces()
			elif map2.lower() in ["no", "No", "Nope", "nope", "nah", "nooo"]:
				sprint("\nMap piece left in box.")
				mapPieces()
		elif box2.lower() in ["no", "No", "Nope", "nope", "nah", "nooo"]:
			sprint("\nThe box has been left alone.")
			mapPieces()
	elif west2 in ["no", "No", "Nope", "nope", "nah", "nooo"]:
		mapPieces()
		
# Define Southeast (Mission Three)
def southeastTwo():
	sprint("\nIt’s a \033[94mbed\033[0m.\n- \033[34mWhere do you want to search? Top or Under?\033[0m -")
	bedLocation = input()
	if bedLocation.lower() in ["bottom", "under"]:
		sprint("\nYou found a \033[94mkey\033[0m. Where do you think you could use this \033[94mkey\033[0m?\n- \033[33mKeep this in your inventory?\033[0m -")
		key2 = input()
		if key2.lower() in ["yes", "Yes", "yeah", "sure", "ok", "alr", "yup", "ye", "ya"]:
			keyTwo + 1
			sprint("\n\033[93m*Added Key to inventory!\033[0m")
			westTwo()
		elif key2.lower() in ["no", "No", "Nope", "nope", "nah", "nooo"]:
			keyTwo + 0
			sprint("\nKey has been left under the bed.")
			westTwopointOne()
	elif bedLocation.lower() in ["top", "Top"]:
		sprint("\nThere's nothing here except a \033[94mpillow\033[0m.\n- \033[33mKeep this in your inventory?\033[0m -")
		pillow = input()
		if pillow.lower() in ["yes", "Yes", "yeah", "sure", "ok", "alr", "yup", "ye", "ya"]:
			sprint("\n\033[93m*Added Pillow to inventory!\033[93m")
			westTwopointOne()
		elif pillow.lower() in ["no", "No", "Nope", "nope", "nah", "nooo"]:
			sprint("\nPillow has been left on top of the bed.")
			westTwopointOne()
# Define Mission Three 
def missionThree():
	time.sleep(1)
	sprint("\n\033[36mMISSION THREE: Find the keys to the locked box.\033[0m")
	time.sleep(1)
	while True:
		sprint("\n- \033[32mGo to Southeast?\033[0m -")
		dire = input()
	
# Question 3
		if dire.lower() in ["yes", "Yes", "yeah", "sure", "ok", "alr", "yup", "ye", "ya"]:
			southeastTwo()
			break
		elif dire.lower() in ["no", "No", "Nope", "nope", "nah", "nooo"]:
			sprint("\n- \033[32mThen where do you want to go?\033[0m -")
			input()
			sprint("\n\033[31mYou can't walk that way.\033[0m")
			continue

# MISSION TWO SECTION

# Window Check
def windowCheck():
	global flashlight
	global batteries
	global mapCollected 
	if flashlight + batteries == 3:
		sprint("\nYou head \033[92mnorth\033[0m to the window.\n- \033[34mUse the flashlight?\033[0m -")
		useOrnot = input()
		if useOrnot in ["yes", "Yes", "yeah", "sure", "ok", "alr", "yup", "ye", "ya"]:
			sprint("\nYou see a \033[94mripped piece of a map\033[0m in between the gap of the \033[94mwindow\033[0m.")
			sprint("- \033[33mDo you wish to keep this in your inventory?\033[0m -")
			keep = input()
			if keep in ["yes", "Yes", "yeah", "sure", "ok", "alr", "yup", "ye", "ya"]:
				sprint("\n\033[93m*Ripped piece of a map added to the inventory!\033[93m")
				mapCollected = mapCollected + 1
				missionThree()
			elif keep in ["no", "No", "Nope", "nope", "nah", "nooo"]:
				sprint("You drop the piece on the ground.")
				missionThree()
		elif useOrnot in ["no", "No", "Nope", "nope", "nah", "nooo"]:
			sprint("Ok then...")
			missionThree()
	elif flashlight + batteries != 3:
		if flashlight == 1:
			sprint("\n\033[31mYou didn't find the batteries.\033[0m")
			sprint("\nPlease try again from the beginning.")
		elif batteries == 2:
			sprint("\n\033[31mYou didn't find the flashlight.\033[0m")
			sprint("\nPlease try again from the beginning.")
			
# Redefine Northwest (Mission 2)
def northwestRE():
	global flashlight
	global batteries
	sprint("\nThere’s a \033[94mcouch\033[0m.\n- \033[34mSearch?\033[0m -")
	couch = input()
	if couch.lower() in ["yes", "Yes", "yeah", "sure", "ok", "alr", "yup", "ye", "ya"]:
		sprint("\nYou search the bottom of the \033[94mcouch\033[0m, there \033[93myou find a flashlight without a battery\033[0m.")
		flashlight = flashlight + 1
		sprint("- Did you find the batteries yet? -")
		didYou2 = input()
		if didYou2 in ["yes", "Yes", "yeah", "sure", "ok", "alr", "yup", "ye", "ya"]:
			windowCheck()
		if didYou2 in ["no", "No", "Nope", "nope", "nah", "nooo"]:
			sprint("\n- \033[32mGo to Southeast?\033[0m - ")
			dire2 = input()
			if dire2.lower() in ["yes", "Yes", "yeah", "sure", "ok", "alr", "yup", "ye", "ya"]:
				southeast()
			if dire2.lower() in ["no", "No", "Nope", "nope", "nah", "nooo"]:
				missionThree()
	elif couch.lower() in ["no", "No", "Nope", "nope", "nah", "nooo"]:
		sprint("\nYou don't search the couch.")
		sprint("\n- \033[32mGo to Southeast?\033[0m - ")
		dire3 = input()
		if dire3.lower() in ["yes", "Yes", "yeah", "sure", "ok", "alr", "yup", "ye", "ya"]:
			southeast()
		if dire3.lower() in ["no", "No", "Nope", "nope", "nah", "nooo"]:
			missionThree()
			flashlight = flashlight + 0

# Define Southeast (Mission 2)
def southeast():
	global flashlight
	global batteries
	sprint ("\nYou then walk \033[92msoutheast\033[0m in hopes of finding more clues. You can make out of what seems like to be a \033[94mbed\033[0m.\n- \033[34mDo you search it?\033[0m -")			
	bed = input()
	if bed.lower() in ["yes", "Yes", "yeah", "sure", "ok", "alr", "yup", "ye", "ya"]:
		sprint("\n\033[93mYou found a battery!!\033[0m Could be used for a \033[94mflashlight\033[0m, you think as you slip it in your pocket.")
		batteries = batteries + 2
		sprint("- Did you find the flashlight yet? -")
		didYou = input()
		if didYou in ["yes", "Yes", "yeah", "sure", "ok", "alr", "yup", "ye", "ya"]:
			windowCheck()
		elif didYou in ["no", "No", "Nope", "nope", "nah", "nooo"]:
			sprint("\n- \033[32mGo to Northwest?\033[0m - ")
			dire3 = input()
			if dire3.lower() in ["yes", "Yes", "yeah", "sure", "ok", "alr", "yup", "ye", "ya"]:
				northwestRE()
			if dire3.lower() in ["no", "No", "Nope", "nope", "nah", "nooo"]:
				missionThree()
	elif bed.lower() in ["no", "No", "Nope", "nope", "nah", "nooo"]:
		sprint("\nYou don't search the bed.")
		batteries = batteries + 0
		sprint("\n- \033[32mGo to Northwest?\033[0m - ")
		dire4 = input()
		if dire4.lower() in ["yes", "Yes", "yeah", "sure", "ok", "alr", "yup", "ye", "ya"]:
			northwestRE()
		if dire4.lower() in ["no", "No", "Nope", "nope", "nah", "nooo"]:
			missionThree()

# Define Northwest (Mission 2)
def northwest():
	global flashlight
	global batteries
	sprint("\nThere’s a \033[94mcouch\033[0m.\n- \033[34mSearch?\033[0m -")
	couch = input()
	if couch.lower() in ["yes", "Yes", "yeah", "sure", "ok", "alr", "yup", "ye", "ya"]:
		sprint("\nYou search the bottom of the \033[94mcouch\033[0m, there \033[93myou find a flashlight without a battery\033[0m.")
		flashlight = flashlight + 1
		sprint("- Did you find the batteries yet? -")
		didYou2 = input()
		if didYou2 in ["yes", "Yes", "yeah", "sure", "ok", "alr", "yup", "ye", "ya"]:
			windowCheck()
		if didYou2 in ["no", "No", "Nope", "nope", "nah", "nooo"]:
			sprint("\n- \033[32mGo to Southeast?\033[0m - ")
			dire2 = input()
			if dire2.lower() in ["yes", "Yes", "yeah", "sure", "ok", "alr", "yup", "ye", "ya"]:
				southeast()
			if dire2.lower() in ["no", "No", "Nope", "nope", "nah", "nooo"]:
				missionThree()
	elif couch.lower() in ["no", "No", "Nope", "nope", "nah", "nooo"]:
		sprint("\nYou don't search the couch.")
		sprint("\n- \033[32mGo to Southeast?\033[0m - ")
		dire3 = input()
		if dire3.lower() in ["yes", "Yes", "yeah", "sure", "ok", "alr", "yup", "ye", "ya"]:
			southeast()
		if dire3.lower() in ["no", "No", "Nope", "nope", "nah", "nooo"]:
			missionThree()
			flashlight = flashlight + 0

# Define Find Flashlight
def findFlashlight():
	while True:
		sprint("\n- \033[32mWhich direction will you choose: Northwest or Southeast?\033[0m -")
		direction = input()
		if direction.lower() in ["northwest", "Northwest", "nw"]:
			northwest()
			break
		elif direction.lower() in ["southeast", "Southeast", "se"]:
			southeast()
			break
		else:
			sprint("\n\033[31mYou can't walk in that direction.\033[0m")
			continue
			
# Redefine Window (Mission 2)
def windowRoute():
	sprint("\nIt’s still dark, but there’s something you feel with the tips of your fingers, it may be dangerous. You wish you could have something to see better.")
	time.sleep(1)
	sprint("\n\033[36mMISSION TWO POINT ONE: Find a flashlight.\033[0m")
	findFlashlight()
			
# Define North (Mission 2)
def northTwo():
	sprint("\n- \033[32mDo you walk to the table or window?\033[0m -")
	walk = input()
	if walk.lower() in ["table", "Table"]:
		while True:
			sprint("\nYou trace your fingers against the surface of the \033[94mtable\033[0m, trying to find any object that may be present on the rough exterior. Nothing seems to be there.")
			sprint("\n- \033[32mWalk to the window?\033[0m -")
			walk2 = input()
			if walk2.lower() in ["yes", "Yes", "yeah", "sure", "ok", "alr", "yup", "ye", "ya"]:
				windowRoute()
				break
			elif walk2.lower() in ["no", "No", "Nope", "nope", "nah", "nooo"]:
				continue
	elif walk.lower() in ["window", "Window"]:
		sprint("\nIt’s still dark, but there’s something you feel with the tips of your fingers, it may be dangerous. You wish you could have something to see better.")
		time.sleep(1)
		sprint("\n\033[36mMISSION TWO POINT ONE: Find a flashlight.\033[0m")
		findFlashlight()

# Define West (Mission 2)
def west():
	global mapCollected 
	sprint("\nHeading to the \033[92mwest\033[0m...You find \033[94mdrawers\033[0m already broken down. \n- \033[34mSearch the drawers?\033[0m -")
	drawer = input()
	if drawer.lower() in ["yes", "Yes", "yeah", "sure", "ok", "alr", "yup", "ye", "ya"]:	
		sprint("\nA \033[94mtorn piece of paper\033[0m falls out with what appears to be intricate drawings of the inside of a house. \n- \033[33mDo you wish to keep this in your inventory?\033[0m -")	
		response = input()
		if response.lower() in ["yes", "Yes", "yeah", "sure", "ok", "alr", "yup", "ye", "ya"]:	
			mapCollected = mapCollected + 1
			sprint("\n\033[93m*Torn Paper added to inventory!\033[0m")
			northTwo()
		elif response.lower() in ["no", "No", "Nope", "nope"]:
			mapCollected = mapCollected + 0
			sprint("\nYou put it back into the \033[94mdrawer\033[0m.")
			northTwo()
	elif drawer.lower() in ["no", "No", "Nope", "nope", "nah", "nooo"]:
		sprint("\nYou don't search the \033[94mdrawer\033[0m.")
		sprint("\n- \033[32mGo North?\033[0m -")
		choose = input()
		if choose.lower() in ["yes", "Yes", "yeah", "sure", "ok", "alr", "yup", "ye", "ya"]:	
			northTwo()
		if choose.lower() in ["no", "No", "Nope", "nope", "nah", "nooo"]:
			sprint("\nHaha too bad, you have no choice.")
			northTwo()
	
# Define East (Mission 2)
def east():
	global mapCollected 
	sprint("\nYou walk into the wall with a \033[94mripped poster\033[0m that looks like a \033[94mmap\033[0m. \n- \033[33mDo you wish to keep this in your inventory?\033[0m -")
	poster = input()
	if poster.lower() in ["yes", "Yes", "yeah", "sure", "ok", "alr", "yup", "ye", "ya"]:
		mapCollected = mapCollected + 1
		sprint("\n\033[93m*Ripped Poster added to inventory!\033[0m")
		west()
	elif poster.lower() in ["no", "No", "Nope", "nope", "nah", "nooo"]:
		mapCollected = mapCollected + 0
		sprint("\nThe \033[94mposter\033[0m is left on the wall.")
		west()
			
# Define Mission Two 
def missionTwo():
	time.sleep(1)
	sprint("\n\033[36mMISSION TWO: Find the missing pieces of the map to plan you grand escape.\033[0m")
	time.sleep(1)
	while True:
		sprint("\n- \033[32mWhich direction will you choose now: East or West?\033[0m -")
		questionTwo = input()
		
# Question 2  
		if questionTwo.lower() in ["east"]:
			east()
			break
		elif questionTwo.lower() in ["west"]:
			west()
			break
		else:
			sprint("\n\033[31mYou can't walk in that direction.\033[91m")
			continue

# MISSION ONE SECTION 

# Define Search Carpet
def searchCarpet():
	sprint("\nYou took a couple of steps back. Your feet trudge against a textile-like material on the ground. You have a feeling it’s an \033[94mold carpet\033[0m.")
	while True:
		sprint("- \033[34mSearch the carpet?\033[0m -")
		carpet = input()
		if carpet.lower() in ["yes", "Yes", "yeah", "sure", "ok", "alr", "yup", "ye", "ya", "yea"]:
			keyOne + 1
			sprint("\n\033[93m*Keys added to inventory!\033[0m")
			keyOne - 1
			sprint("\nYou rush to the \033[94mlocked window\033[0m, inserting the \033[94mkeys\033[0m you find yourself staring at the same darkness outside as the inside...")
			sprint("- \033[34mDo you wish to climb out of the window?\033[0m -")
			window = input()
			if window.lower() in ["yes", "Yes", "yeah", "sure", "ok", "alr", "yup", "ye", "ya"]:
				sprint("\n\033[31mOUCH you fell to your death!\033[0m")
				break
			elif window.lower() in ["no", "No", "Nope", "nope", "nah", "nooo"]:
				sprint("\nYou walked away from the \033[94mwindow\033[0m.")
				missionTwo()
				break
		elif carpet.lower() in ["no", "No", "Nope", "nope", "nah", "nooo"]:
			sprint("\nYou stare at the \033[94mlocked window\033[0m. You still think you need to search the \033[94mcarpet\033[0m.")
			continue
		
			
# Define South (Mission 1)
def south():
	sprint("\nYou walk \033[92msouth\033[0m and stumble into a \033[94mshelf\033[0m. \n- \033[34mSearch the shelf?\033[0m -")
	shelf = input()
	if shelf.lower() in ["yes", "Yes", "yeah", "sure", "ok", "alr", "yup", "ye", "ya"]:
		sprint("\nYou peer your eyes into the \033[94mshelf\033[0m and shift your fingers through each crevice. Your hands feel a \033[94mwooden box\033[0m situated in the left corner of the second level of the \033[94mshelf\033[0m.")
		sprint("\nYou hold the \033[94mbox\033[0m, inspecting its every crevice. No matter how hard you tried to open it, it wouldn’t budge. \n- \033[33mKeep in inventory?\033[0m -")
		box = input()
		if box.lower() in ["yes", "Yes", "yeah", "sure", "ok", "alr", "yup", "ye", "ya"]:
			lockedBox + 1
			sprint("\n\033[93m*Box added to inventory!\033[0m")
			searchCarpet()
		elif box.lower() in ["no", "No", "Nope", "nope", "nah", "nooo"]:
			lockedBox + 0
			sprint("\nYou put the \033[94mbox\033[0m back on the \033[94mshelf\033[0m.")
			searchCarpet()
	elif shelf.lower() in ["no", "No", "Nope", "nope", "nah", "nooo"]:
		searchCarpet()

# Define North (Mission 1)
def north():
	sprint("\nYou take a couple of steps forward but crash into a \033[94mtable\033[0m. \n- \033[34mSearch the table?\033[0m -")
	table = input()
	if table.lower() in ["yes", "Yes", "yeah", "sure", "ok", "alr", "yup", "ye", "ya"]:						
		sprint("\nYou searched above and under the \033[94mtable\033[0m, but nothing is there.")
		while True:
			sprint("- \033[32mGo South?\033[0m -") 
			answer = input()
			if answer.lower() in ["yes", "Yes", "yeah", "sure", "ok", "alr", "yup", "ye", "ya"]:	
				south()
				break
			elif answer.lower() in ["no", "No", "Nope", "nope", "nah", "nooo"]:
				sprint("\nBut there is nothing there.")
				continue
	elif table.lower() in ["no", "No", "Nope", "nope", "nah", "nooo"]:
			while True:
				sprint("\nYou don't inspect the \033[94mtable\033[0m. Other than the \033[94mtable\033[0m there is nothing there.\n- \033[32mGo South?\033[0m -")
				answer2 = input()
				if answer2.lower() in ["yes", "Yes", "yeah", "sure", "ok", "alr", "yup", "ye", "ya"]:	
					south()
					break
				elif answer2.lower() in ["no", "No", "Nope", "nope", "nah", "nooo"]:
					sprint("\nBut...")
					continue

# Define Mission One
def missionOne():
	time.sleep(1)
	sprint("\033[36mMISSION ONE: Find the key to the locked window.\033[0m\n")
	time.sleep(1)
	sprint("You get up from the wooden floor and decide to figure out which direction to go.") 
	while True:
		sprint("- \033[32mWhich way will you walk: North or South?\033[0m -")
		questionone = input()

# Question 1
		if questionone.lower() in ["north", "n"]:
			north()
			break
		elif questionone.lower() in ["south", "s"]:
			south()
			break
		else:
			sprint("\n\033[31mYou can't walk in that direction.\033[91m")
			continue

# Intro
sprint("You woke up in a dim, dark room without a singLe sliver of light. A deafening silence fills the room. Everything is still. Nobody is here except for you. Perplexed, you examine your surroundings to grasp the situation. \033[4mYou can make out a chained door and a locked window and a couple of other items, but it’s pitch dark.\033[0m\n")

# Mission One
missionOne()