"""
exercise : Electronic shop.

Function should return maximum amount she can spent
on keyboard and drive if she can't buy anything 
then return -1

"""
def getMoneySpent(keyboards, drives, b):
	max_spent = []
	for keyboard in keyboards:
		for drive in drives:
			if ((price := keyboard + drive) <= b):
				max_spent.append(price)

	if len(max_spent) == 0:
		return -1
	else :
		return max(max_spent)

print(getMoneySpent([3,1], [5,2,8], 10))
