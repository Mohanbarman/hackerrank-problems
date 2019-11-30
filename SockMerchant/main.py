def sockMerchant(arr, n):
	pair = 0

	socks_map = {sock: arr.count(sock) for sock in arr}

	for sock_count in socks_map.values():
		if sock_count > 1:
			pair += (sock_count - sock_count%2)//2

	return pair

# 6 5 2 3 5 2 2 1 1 5 1 3 3 3 5

socks = list(map(int, input().split()))

print(sockMerchant(socks, 1))