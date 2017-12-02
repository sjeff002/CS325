import sys
from collections import defaultdict

with open("input.txt", "r") as myFile:
	numWrestler = myFile.readline().strip('\n').split(" ")
	numWrestler = int(numWrestler[0])
	print(numWrestler)
	wrestlers = []
	for x in range(0, numWrestler):
		temp = myFile.readline().strip('\n').split(" ")
		temp = temp[0]
		wrestlers.append(temp)
	numRivalries = myFile.readline().strip('\n').split(" ")
	numRivalries = int(numRivalries[0])
	rivalries = []
	print(numRivalries)
	for x in range(0, numRivalries):
		rivalries.append(myFile.readline().strip('\n').split(" "))

myAdjList = defaultdict(list)

for a, b in rivalries:
    myAdjList[a].append(b)
    myAdjList[b].append(a)
    

def isValid(myList, allW):
	babyfaces = set()
	heels = set()

	for vert, neighbors in myList.items():
		if vert in babyfaces:
			for neighbor in neighbors:
				heels.add(neighbor)
		elif vert in heels:
			for neighbor in neighbors:
				babyfaces.add(neighbor)
		else:
			babyfaces.add(vert)
			for neighbor in neighbors:
				heels.add(neighbor)

	for x in allW:
		if not x in babyfaces and not x in heels:
			babyfaces.add(x)

	truth = not bool(babyfaces.intersection(heels))
	return truth, babyfaces, heels



answer, babyfaces, heels = isValid(myAdjList, wrestlers)

if answer:
	print "Yes"
	babyfaces = list(babyfaces)
	mystr = " ".join(babyfaces)
	print "Babyfaces:", mystr
	heels = list(heels)
	mystr = " ".join(heels)
	print "Heels:", mystr
else:
	print "No"