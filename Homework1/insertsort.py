######################################################################################
#Author: Shannon Jeffers
#Class: CS 325 Analysis of Algorithms
#Homework # 1 Problem 4 part a
#Program: This is a Python version of InsertSort derived from the book's psudocode
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

#insertSort sorts a list by insertion
def insertSort(myList):
	#goes through every element from 1 (the second element) to the length
	for num in range(1, len(myList)):
		cur = myList[num]
		temp = num - 1
		#while we arent at the front of the list or the element to the left
		#of the element we are looking for isn't bigger.
		while temp > -1 and myList[temp] > cur:
			#swap the elements.
			myList[temp + 1] = myList[temp]
			myList[temp] = cur
			temp -= 1


#collects the time it takes to run 
start = time.time()
for l in myList:
	insertSort(l)
end = time.time()

print(end - start)

outFile = open("insert.out", "w")

#retransforms the data into a string
for l in myList:
	l = map(str, l)
	myString = " ".join(l)
	outFile.write(myString)
	outFile.write("\n")


outFile.close()