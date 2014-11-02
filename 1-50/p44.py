import euler

def pentagon(i) :
	return i * (3 * i - 1) // 2

def solution():
	i = 1
	while True:
		i += 1
		k = pentagon(i)
		for t in range(i - 1, 0, -1):
			j = pentagon(t)
			if euler.is_pentagon_number(k - j) and euler.is_pentagon_number(j + k):
				print('solution : j = %d, k = %d, D = %d' % (j, k, k - j))
				return
solution()