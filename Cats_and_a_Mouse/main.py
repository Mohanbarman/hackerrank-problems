"""
exercise : cats and a mouse.

cat A = 1
cat B = 5
Mouse = 3

Cat A __ Mouse __ Cat B.

you have to determine which cat will catch the mouse first.

"""
def catAndMouse(x, y, z):
	catA = abs(x - z)
	catB = abs(y - z)

	if catA < catB :
		return "Cat A"
	else :
		return "Cat B"
