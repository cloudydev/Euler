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

# check whether d is palindromic
def is_palindromic(d):
	return reverse_digits(d) == d

# reverse digits in d. eg. 1292 -> 2921
def reverse_digits(d):
	r = 0
	while d:
		r = 10 * r + d % 10
		d = d // 10
	return r

# check whether n is a prime number
def is_prime(n):
	if n <= 0:
		return False
	if n % 2 == 0 and n > 2:
		return False
	return all(n % i for i in range(3, int(math.sqrt(n) + 1), 2))

# select r from n items
def combinatoric_select(n, r):
	if r == 0 or n == r:
		return 1
	t = 1;
	for x in range(r):
		t *= (n - x)
	return t // math.factorial(r)

# return the number of digits
def digit_length(d):
	l = 0
	while d:
		l += 1
		d = d // 10
	return l






