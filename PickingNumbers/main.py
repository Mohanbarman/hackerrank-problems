"""
exercise : Picking numbers.

form arrays from an given array where diffrence of any two 
number is less than or equals to 1 . 
Then return the lenght of those arrays which have 
maximum elements.

time complexity = O(n^2)

"""
# def pickingNumbers(array):

# 	array.sort()
# 	picked_arrays = []
# 	current_array = []

# 	temp = []

# 	for counter, x in enumerate(array):
# 		if x + 1 == array[counter + 1]:


# 	return picked_arrays

# print(pickingNumbers([1, 1, 2, 2, 4, 4, 5, 5, 5]))

# n = int(input())
# l = [ int(i) for i in input().split() ]
# maximum = 0
# for i in l:
#     c = l.count(i)
#     d = l.count(i-1)
#     c = c+d
#     if c > maximum:
#             maximum = c
# print(maximum)

# one line 

arr = [1,2,3,2,2,1]

print(max([arr.count(i) + arr.count(i - 1) for i in arr]))