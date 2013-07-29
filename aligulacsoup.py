from bs4 import BeautifulSoup
import urllib
import random

def aligulacsoup(p1, p2, x):
	prefix = "http://www.aligulac.com/predict/match/?bo=1&ps="
	player1 = str(p1)
	player2 = str(p2)
	opener = 'http://www.aligulac.com/players/'
	name1 = simplelookup(player1)
	name2 = simplelookup(player2)
	boX = x
	nothing = player1 + '%2C' + player2
	text = urllib.urlopen(prefix + nothing).read()
	soup = BeautifulSoup(text)
	results = soup.select(".rowh .rowe")
	firstresult = results[0].string.encode('utf-8')
	result1 = float(firstresult.strip('%'))
	secondresult = results[4].string.encode('utf-8')
	result2 = float(secondresult.strip('%'))
	wins1, wins2 = simulate(result1, result2, boX)
	if wins1 > wins2:
		winner = player1
	if wins2 > wins1:
		winner = player2
	return wins1, wins2, name1, name2, winner

def simulate(result1, result2, boX):
	wins1 = 0
	wins2 = 0
	while True:
		random.seed()
		ourresult = random.random()
		if ourresult < (result1 / 100):
			wins1 += 1
		elif ourresult >= (result1 / 100):
			wins2 += 1
		if (float(wins1) / boX) > 0.5 or (float(wins2) / boX) > 0.5:
			break
	return wins1, wins2
	
def simplelookup(name1):
	opener = 'http://www.aligulac.com/players/'
	soup1 = BeautifulSoup(urllib.urlopen(opener + name1).read())
	return soup1.title.string.encode('utf-8')

