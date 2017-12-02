#########################################################################################################
##Name: Shannon Jeffers
##Assignment: Homework 2 number 5 part a
#########################################################################################################
from collections import deque
from collections import defaultdict
import sys

#open file from command line, handles file closing
with open(sys.argv[1], "r") as myFile:
	#read in number of wrestlers
	numWrestler = myFile.readline().strip('\n').split(" ")
	numWrestler = int(numWrestler[0])
	wrestlers = []
	#read in each wrestler name
	for x in range(0, numWrestler):
		temp = myFile.readline().strip('\n').split(" ")
		wrestlers.append(temp[0])
	# read in number of rivalries
	numRivalries = myFile.readline().strip('\n').split(" ")
	numRivalries = int(numRivalries[0])
	rivalries = []
	#read in each rivalry pair
	for x in range(0, numRivalries):
		rivalries.append(myFile.readline().strip('\n').split(" "))
teams = {}
checked = {}

#create a dictionary of lists
rivals = defaultdict(list)
#fill dictionary of lists with rivalries
for a, b in rivalries:
    rivals[a].append(b)
    rivals[b].append(a)
#set up teams and checked to default values
for w in wrestlers:
	teams[w] = 0
	checked[w] = 0

def isValid(teams, rivals, w, c, s):
	Q = deque()
	Q.append(s)
	#while there is an item in the queue
	while Q:
		#remove the first item
		u = Q.popleft()
		#indicate it has been checked
		c[u] = 1
		#if it doesnt have a team, make it a babyface
		if teams[u] == 0:
			teams[u] = "Babyface"
		#loop through all its rivals
		for rival in rivals[u]:
			#if rival doesnt have a team make it opposite of u
			if teams[rival] == 0:
				if teams[u] == "Babyface":
					teams[rival] = "Heel"
				else:
					teams[rival] = "Babyface"
			#if it does have a team and the team is the same as u this graph isnt correct
			if teams[u] == teams[rival] and teams[rival] != 0:
				return False
			#if the rival hasnt been checked, add it to the queue
			if c[rival] == 0:
				Q.append(rival)
	#if we made it this far, graph is fine!
	return True

babyface = []
heels = []
#loop through teams to place wrestlers in their porper team
for key in teams:
	if teams[key] == "Babyface":
		babyface.append(key)
	elif teams[key] == "Heel":
		heels.append(key)
	else:
		answer = isValid(teams, rivals, wrestlers, checked, key)
		if teams[key] == "Babyface":
			babyface.append(key)
		elif teams[key] == "Heel":
			heels.append(key)
	if not answer:
		break;

print (answer)
if answer:
	mystr = " ".join(babyface)
	print ("Babyfaces:", mystr)
	mystr = " ".join(heels)
	print ("Heels:", mystr)