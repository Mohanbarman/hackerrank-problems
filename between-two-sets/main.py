"""
HACKERRANK - Between Two Sets

Conditions :

	1. All numbers in first array are factors of x.
		* x%array[n]
	2. X is factor of all numbers in second array.
		* array[n]%x

These numbers are reffered to between two arrays.

Algotithm:

Step 1. Find all numbers which are which evenly get devided by all the elements  		 of first array to the range of max number in second array.

Step 2. From those numbers find all numbers which divide all elements of second 		 array evenly.

"""
def getTotalX(firstArray, secondArray):
	factorFirst = []
	factorSecond = []

	for i in range(1, max(secondArray) + 1):
		if all(list(map(lambda x: i%x == 0, firstArray))):
			factorFirst.append(i)

	for i in factorFirst:
		if all(list(map(lambda x: x%i == 0, secondArray))):
			factorSecond.append(i)

	return len(factorSecond)

print(getTotalX([1],[100]))
