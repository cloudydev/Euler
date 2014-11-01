import math
import euler

primes = euler.primes(2, 1000000)
cache = {x : True for x in primes}
def is_prime(n):
	return n in cache

def digit_len(n):
	l = 0
	while n:
		n = n // 10
		l += 1
	return l

def is_circular_prime(n):
	digits = digit_len(n)
	scale = int(math.pow(10, digits - 1))
	for i in range(0, digits):
		unit = n % 10
		n = unit * scale + n // 10
		if not is_prime(n):
			return False
	return True

assert is_circular_prime(197)
assert is_circular_prime(97)

result = [x for x in primes if is_circular_prime(x)]
print(result)
print(len(result))

