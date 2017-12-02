import time
from random import randint

#n = int(input("Enter a number for n: "))
n=7000
myList = []

for x in range(n):
	i = randint(1,10000)
	myList.append(i)


#insertSort sorts a list by insertion
def stoogesort(myList, low, high):
	n = high-low + 1
	if myList[low] > myList[high]:
		myList[low], myList[high] = myList[high], myList[low]
	if n > 2:
		m = int(n/3.0)
		stoogesort(myList, low, high-m)
		stoogesort(myList, low+m, high)
		stoogesort(myList, low, high-m)


#collects the time it takes to run 
start = time.time()
stoogesort(myList, 0, (len(myList)-1))
end = time.time()

print(end - start)