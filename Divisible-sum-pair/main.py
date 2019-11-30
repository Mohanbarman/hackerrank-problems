def divisibleSumPair(n, k, ar):
	ways = 0

	for i in range(n):
		for j in range(n):
			if i < j:
				if (ar[i] + ar[j])%k == 0:
					print('worked')
					ways += 1
	
	return ways