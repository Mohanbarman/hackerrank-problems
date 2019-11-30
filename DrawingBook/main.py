# task :-
"""
pages : (1),(2,3),(4,5),(n-1,n)

"""

def pageCount(numOfPages ,pageNumber):
	pages = []
	
	for pagenum in range(0, numOfPages + 1, 2):
		if (pagenum == numOfPages):
			pages.append([pagenum])
			continue
		pages.append([pagenum, pagenum + 1])

	for index, page in enumerate(pages):
		if pageNumber in page:
			pageFromLeft = index

	for index, page in enumerate(pages[::-1]):
		if pageNumber in page:
			pageFromRight = index

	return min(pageFromRight, pageFromLeft)

p = int(input("Enter total number of pages : "))
n = int(input("Enter page number to turn : "))

print(pageCount(p,n))
