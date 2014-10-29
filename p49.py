import euler

primes = euler.primes(1000, 9999)

def is_prime(n):
	return n in primes

def is_permutation(a, b):
	l = [0 for i in range(10)]
	while a:
		l[a % 10] += 1
		l[b % 10] -= 1
		a = a // 10
		b = b // 10
	return all(x == 0 for x in l)

assert is_permutation(1487, 4817)

for i in range(len(primes)):
	for j in range(i + 1, len(primes)):
		a = primes[i]
		b = primes[j]
		c = 2 * b - a
		if is_prime(c) and is_permutation(a, b) and is_permutation(a, c):
			print('find permutation (%d, %d, %d)' % (a, b, c))