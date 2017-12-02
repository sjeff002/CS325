#########################################################################################################
##Name: Shannon Jeffers
##Assignment: Homework 2 number 5 part a
#########################################################################################################

import time
import math


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


# this is a python modification of the psudocode from wiki https://en.wikipedia.org/wiki/Stooge_sort
# also uses 2/3rds of the array, the indexes are just easier.
def stoogesort(myList, low, high):
	n = high-low + 1
	if myList[low] > myList[high]:
		myList[low], myList[high] = myList[high], myList[low]
	if n > 2:
		m = int(n/3.0)
		stoogesort(myList, low, high-m)
		stoogesort(myList, low+m, high)
		stoogesort(myList, low, high-m)


start = time.time()
for l in myList:
	stoogesort(l, 0, (len(l)-1))
end = time.time()

print(end - start)

outFile = open("stooge.out", "w")

#retransforms the data into a string
for l in myList:
	l = map(str, l)
	myString = " ".join(l)
	outFile.write(myString)
	outFile.write("\n")


outFile.close()