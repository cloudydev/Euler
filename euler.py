import math

# check whether d is a triangle number
def is_triangle_number(d):
	double = 2 * d
	upper = int(math.sqrt(double)) + 1
	for i in range(1, upper + 1):
		if i * (i + 1) == double:
			return True
	return False

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