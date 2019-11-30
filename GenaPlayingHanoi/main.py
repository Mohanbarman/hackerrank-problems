import sys

# Gena playing hanoi #

N = int(input())
if N > 10 :
	print('N cannot be greater than 10')
	sys.exit(100)	
a = list(map(int, input().rstrip().split()))

def calc_min_moves(a):

	# Rods 
	r1 = []
	r2 = []
	r3 = []
	r4 = []

	#This function will fill the rods

	def fill_rods(): 
		for disc, index in enumerate(a) :
			if index == 1:
				r1.append(disc + 1)	
			elif index == 2:
				r2.append(disc + 1)
			elif index == 3:
				r3.append(disc + 1)
			elif index == 4:
				r4.append(disc + 1)

		r1.sort()
		r2.sort()
		r3.sort()
		r4.sort()

	rods = [r1, r2, r3, r4]

	def get_rod(index):
		if index == 0:
			return r1
		elif index == 1:
			return r2
		elif index == 2:
			return r3
		elif index == 3:
			return r4

	# This function will return the base rod (Where we will arrange all the discs)

	def find_base_rod() :
		max_num = max(r1 + r2 + r3 + r4)
		for counter, rod in enumerate(rods) :
			if max_num in rod :
				return get_rod(index)	

	def arrange_discs(base_rod):
		moves = 0
		next_disc = max(base_rod) - 1
		for counter, rod in enumerate(rods) :
			if next_disc in base_rod :
				next_disc = next_disc + 1
			else :
				