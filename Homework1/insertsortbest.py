##Shannon Jeffers extra credit

import time
from random import randint

#n = int(input("Enter a number for n: "))
n=10000
myList = []

for x in range(n):
	myList.append(x)


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