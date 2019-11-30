"""

* s -- t -> distance of house.
* a -> apple tree.
* b -> orange tree.
* d -> distance of fruit from tree.

"""

def countApplesAndOranges(s, t, a, b, apples, oranges):
	distance_of_apple_from_tree = [apple + a for apple in apples]
	distance_of_orange_from_tree = [orange + b for orange in oranges]

	apples_in_house = 0
	oranges_in_house = 0

	for apple_pos in distance_of_apple_from_tree:
		if (s <= apple_pos <= t):
			apples_in_house += 1
	
	for orange_pos in distance_of_orange_from_tree:
		if (s <= orange_pos <= t):
			oranges_in_house += 1

	print(apples_in_house)
	print(oranges_in_house)