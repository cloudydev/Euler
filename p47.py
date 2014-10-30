import euler
import math

primes = euler.primes(2, 1000)
def distinct_prime_factors(n):
	half = n // 2
	return sum(1 for x in primes if x <= half and n % x == 0)

def solution():
	i = 2 * 3 * 5 *7
	while True:
		for j in range(4):
			if distinct_prime_factors(i + j) != 4:
				i += j + 1
				break
			if j == 3: #Find a solution
				print('solution is %d' % i)
				return
solution()