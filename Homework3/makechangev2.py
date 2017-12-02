import time
import sys

V = []
for i in range(0, 100000):
	V.append(i)

A = 100000


#function that determines the minumum amount of coins to make change.
def makeChange(V, A):
	numCoins = []
	index = []
	numCoins.append(0)
	index.append(0)
	#set all values in numCoins high so the first time we find a coin
	#that can make the value it will be lower than the value that is present
	#set all index's lower than the lowest index
	for i in range(0, A):
		numCoins.append(sys.maxsize-1)
		index.append(-1)
	#Go through every value from 1-A for each coin
	for j in range(0, len(V)):
		for i in range(1, A+1):
			#if the value is greater or equal to the denomination of the current coin
			if i >= V[j]:
				#if the new number of coins it takes to make a value is smaller than the old one
				if numCoins[i-V[j]] + 1 < numCoins[i]:
					#replace the number of coins it takes to make a value
					numCoins[i] = numCoins[i-V[j]] + 1
					#store the index of the last coin used to make the value
					index[i] = j
	C = []
	#this array will tell us how many of each coin was used
	for i in range(0,len(V)):
		C.append(0)
	total = A
	#trace backwards to figure out the count of each coin used.
	while total != 0:
		C[index[total]] += 1
		total = total - V[index[total]]
	return C, numCoins[A]

coin = []
start = time.time()
coin, mincoin = makeChange(V,A)
end = time.time()

print(end - start)