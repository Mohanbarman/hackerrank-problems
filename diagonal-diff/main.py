matrix = []

for _ in range(int(input())):
	row = list(map(lambda x : int(x),input('Enter a row -> ').split(' ')))
	matrix.append(row)

ltr = 0
rtl = 0
i = 0

for row in matrix:
	ltr += row[i]
	i += 1

i = len(matrix[1]) - 1
for row in matrix:
	rtl += row[i]
	i -= 1

print(rtl - ltr)