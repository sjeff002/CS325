######################################################################################
#Author: Shannon Jeffers
#Class: CS 325 Analysis of Algorithms
#Homework # 1 Problem 4 part b
#Program: This is a Python version of mergesort derived from the book's psudocode
######################################################################################
import time

myFile = open("data.txt", "r")
myList = []
#This gets the data from the file, removes "splits" the spaces to store each number as list elements
#and then converts each of those elements into a number from a string.
i = 0
while 1:
	myData = myFile.readline().strip('\n').split(" ")
	if not myData[0]:
		break
	myData = map(int, myData)
	del myData[0]
	myList.append(myData)
	i += 1


myFile.close()

#merges two sorted lists into 1 sorted list
def merge(list1, list2):
	sorted = []
	i = 0
	j = 0
	#while both lists have not made it to the end
	while i != len(list1) and j != len(list2):
		# if the element in list 1 is smaller, add it to the sorted list
		if list1[i] < list2[j]:
			sorted.append(list1[i])
			i += 1
		#else add the element from list 2 to the sorted list
		else:
			sorted.append(list2[j])
			j += 1
	#if some elements remian in list 1 add them all to the sorted list
	if i < len(list1):
		while i < len(list1):
			sorted.append(list1[i])
			i += 1
	#if some elements remain in list 2 add them all to the sorted list
	else:
		while j < len(list2):
			sorted.append(list2[j])
			j += 1
	return sorted

#mergesort calls itself recursively until there is 1 or fewer items in each list
#it then merges the two lists together.
def mergeSort(myList):
	if len(myList) < 2:
		return myList
	mid = len(myList)/2
	list1 = mergeSort(myList[:mid])
	list2 = mergeSort(myList[mid:])
	return merge(list1, list2)

newList = []
#collects the time it takes to run 
start = time.time()
for l in myList:
	new = mergeSort(l)
	newList.append(new)
end = time.time()

print(end - start)

outFile = open("merge.out", "w")

#retransforms the data into a string
for l in newList:
	l = map(str, l)
	myString = " ".join(l)
	outFile.write(myString)
	outFile.write("\n")

outFile.close()