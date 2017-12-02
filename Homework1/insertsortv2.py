######################################################################################
#Author: Shannon Jeffers
#Class: CS 325 Analysis of Algorithms
#Homework # 1 Problem 4 part a
#Program: This is a Python version of InsertSort derived from the book's psudocode
######################################################################################
import time
from random import randint

#n = int(input("Enter a number for n: "))
n=7000
myList = []

for x in range(n):
	i = randint(1,10000)
	myList.append(i)


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
insertSort(myList)
end = time.time()

print(end - start)

outFile = open("insert.out", "w")

#retransforms the data into a string
myList = map(str, myList)
#joins all list elements together as a string with spaces between
myString = " ".join(myList)

outFile.write(myString)

outFile.close()