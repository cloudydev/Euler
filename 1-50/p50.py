# Consecutive prime sum
import euler

limit = 1000000
primes = euler.primes(2, limit)
sums = [0]
for p in primes:
	sums.append(sums[-1] + p if len(sums) > 0 else p)

cache = {x : True for x in primes}
def is_prime(x):
	return x in cache

def solution():
	result = list()
	# possible number of items
	for i in range(2, len(primes)):
		for j in range(len(primes) - i + 1):
			# sonsecutive sum begin with the jth prime and length i
			sum_j = sums[j + i] - sums[j]
			# early return
			# all subsequent sums begin with j will beyond limit
			if sum_j >= limit:
				if j != 0:
					break # escape the inner loop					
				else:
					# escape the outer loop
					# we cannot find any sum with length greater than i any more
					return result 

			if is_prime(sum_j):
				result.append(primes[j:j + i])
	return result

for r in solution():
	print('sum: %d, length: %d.' % (sum(r), len(r)))