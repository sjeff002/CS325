#################################################################################################
##Author: Shannon Jeffers
## Class: CS325
## Assignment:  Homework 4
#################################################################################################

#insertSort sorts a list by insertion
#merges two sorted lists into 1 sorted list
def merge(list1, list2):
	mySorted = []
	i = 0
	j = 0
	#while both lists have not made it to the end
	while i != len(list1) and j != len(list2):
		# if the element in list 1 is smaller, add it to the sorted list
		if list1[i][1] >= list2[j][1]:
			mySorted.append(list1[i])
			i += 1
		#else add the element from list 2 to the sorted list
		else:
			mySorted.append(list2[j])
			j += 1
	#if some elements remian in list 1 add them all to the sorted list
	if i < len(list1):
		while i < len(list1):
			mySorted.append(list1[i])
			i += 1
	#if some elements remain in list 2 add them all to the sorted list
	else:
		while j < len(list2):
			mySorted.append(list2[j])
			j += 1
	return mySorted

#mergesort calls itself recursively until there is 1 or fewer items in each list
#it then merges the two lists together.
def mergeSort(myList):
	if len(myList) < 2:
		return myList
	mid = len(myList)/2
	list1 = mergeSort(myList[:mid])
	list2 = mergeSort(myList[mid:])
	return merge(list1, list2)


def greedySelect(tasks):
	tasks = mergeSort(tasks) #sort tasks by descending start time
	n = len(tasks)
	A = []
	A.append(tasks[0][0]) #Add the first task. Key to the greedy algorithm!
	k = 0
	for m in range(1, n):
		if tasks[k][1] >= tasks[m][2]: # if the finish time of the next task is before the start time of the previous
			A.append(tasks[m][0]) #its compatable, add it!
			k = m
	return A

myFile = open("act.txt", "r")
setCount = 0

while 1:
	#get the number of activities in the set
	count = myFile.readline().strip('\n').strip('\r').split(" ")
	if not count[0]:
		break
	setCount += 1
	count = map(int, count)
	count = count[0]
	myList = []
	#read in each of those activities
	for j in range (0, count):
		myData = myFile.readline().strip('\n').strip('\r').split(" ")
		if not myData[len(myData)-1]:
			myData = myData[:-1]
		myData = map(int, myData)
		myList.append(myData)
	#myList.sort(key=lambda x: x[1], reverse = True)
	activities = greedySelect(myList)
	print 'Set ', setCount
	print'Number of activities selected =', len(activities)
	activities = map(str, activities)
	activities.reverse()
	activities = " ".join(activities)
	print'Activities:', activities, '\n'

myFile.close()