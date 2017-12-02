##Shannon Jeffers Extra Credit
## the mixup function was inspired by https://stackoverflow.com/questions/24594112/when-will-the-worst-case-of-merge-sort-occur

import time
from random import randint

#n = int(input("Enter a number for n: "))
n=1000
myList = []

for x in range(n):
	myList.append(x)

#for worse case we want every element to be evaluated
#we want equal amounts of the "largest" elements on both sides and smaller elements between them
def mixup(myList):
	#if our list is 1 or less we do nothing
	if len(myList) <= 1:
		return myList
	#if our list has 2 elements, swap em
	if len(myList) == 2:
		temp = myList[0]
		myList[0] = myList[1]
		myList[1] = temp
		return myList
	left = []
	right = []
	#in all other cases store every other element in a
	# left or right sub array
	for i in range(0, len(myList), 2):
		left.append(myList[i])
	for i in range(1, len(myList), 2):
		right.append(myList[i])
	#call mixup again to mix up sub arrays and split them into smaller arrays
	left = mixup(left)
	right = mixup(right)
	#combine the left and right mixed up sub arrays
	myList = left + right
	return myList

myList = mixup(myList)

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