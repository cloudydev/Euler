coins = [1, 2, 5, 10, 20, 50, 100, 200]

def find_ways(n):
	ways = [1 if x == 0 else 0 for x in range(0, n + 1)]
	# i means the max coin we can use
	for i in coins:
		for j in range(i, n + 1):
			ways[j] = ways[j] + ways[j - i]
	return ways[n]

print(find_ways(2 * 100))