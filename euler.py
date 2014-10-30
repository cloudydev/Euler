import math

# check whether d is a triangle number
# k(k + 1) / 2 = n
def is_triangle_number(n):
	k = int((math.sqrt(1 + 8 * n) - 1) / 2)
	return k * (k + 1) // 2 == n

# check whether n is a pentagon number
# k(3k-1) / 2 = n
def is_pentagon_number(n):
	k = int((math.sqrt(1 + 24 * n) + 1) / 6)
	return k * (3 * k - 1) // 2 == n

# check whether d is a pandigital using consecutive digits [start, end]
def is_pandigital(d, start = 1, end = 9):
	used = [0 for x in range(end - start + 1)]
	while d:
		r = d % 10
		d = d // 10
		if r not in range(start, end + 1):
			return False
		used[r - start] += 1
	return all(used) and sum(used) == end - start + 1

# generate primes between start and end [start, end]
def primes(start, end):
	array = [True for x in range(0, end + 1)]
	for i in range(2, int(math.sqrt(end) + 1) + 1):
		if array[i]:
			j = i + i
			while j <= end:
				array[j] = False
				j += i
	return [x for x in range(2, end + 1) if array[x] and x >= start]