"""

* Kangaroo 1:
	* x1 = start position.
	* v1 = end position.
* Kangaroo 2:
	* x2 = start position.
	* v2 = end position.

"""


def kangaroo(x1, v1, x2, v2):

	while True:
		if x1 > x2 :
			if v1 > v2 or v1 == v2 :
				return 'NO'
			else :
				x1 += v1
				x2 += v2

		elif x1 < x2 :
			if v1 < v2 or v1 == v2:
				return 'NO'
			else :
				x1 += v1
				x2 += v2

		if x1 == x2 :
			return 'YES'
		