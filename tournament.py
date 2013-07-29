import aligulacsoup
from math import log

def playerinput():
	newplayer = input("Enter a list of numerical Aligulac IDs, separated by commas: ")
	playerlist = list(newplayer)
	return playerlist
	
players = playerinput()
while True:
	if log(len(players), 2).is_integer():
		rounds = int(log(len(players), 2))
		break
	else:
		print("Number of players needs to be a power of 2.")
		players = playerinput()
		
		
rlength = []

for i in range(rounds):
	while True:
		length = input("Enter length of round " + str(i + 1) + ": ")
		if length % 2 == 0:
			print("Series length must be odd!")
		else:
			break
	rlength.append(length)
	
nextplayers = []
currentRound = 0

while (len(players) % 2) == 0:
	print('')
	for i in range(len(players)/2):
		wins1, wins2, name1, name2, winner = aligulacsoup.aligulacsoup(players[2*i], players[2*i + 1], rlength[currentRound])
		if wins1 > wins2:
			print(name1 + " " + str(wins1) + "-" + str(wins2) + " " + name2)
		if wins2 > wins1:
			print(name2 + " " + str(wins2) + "-" + str(wins1) + " " + name1)
		nextplayers.append(winner)
	players = nextplayers
	nextplayers = []
	currentRound += 1
	

if len(players) > 1:
	print("Odd number of players!")
elif len(players) == 1:
	name = aligulacsoup.simplelookup(players[0])
	print(name + " is the winner!")
