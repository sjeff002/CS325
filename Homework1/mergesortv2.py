import time
from random import randint

#n = int(input("Enter a number for n: "))
n=7000
myList = []

for x in range(n):
	i = randint(1,10000)
	myList.append(i)


#insertSort sorts a list by insertion
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


#collects the time it takes to run 
start = time.time()
myList = mergeSort(myList)
end = time.time()

print(end - start)

#outFile = open("insert.out", "w")

#retransforms the data into a string
#myList = map(str, myList)
#joins all list elements together as a string with spaces between
#myString = " ".join(myList)

#outFile.write(myString)

#outFile.close()