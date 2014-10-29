import euler
import math
primes = euler.primes(2, 100000)

def is_twice_square(n):
	if n % 2 == 1:
		return False
	n = n // 2
	s = int(math.sqrt(n))
	return s * s == n

def meet_conjecture(n):
	for i in primes:
		if i <= n and is_twice_square(n - i):
			return True
	return False

assert meet_conjecture(27)
odd = 35

while True:
	if not meet_conjecture(odd):
		print('Solution: %d' % odd)
		break
	odd += 2