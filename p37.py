import euler
primes = euler.primes(2, 1000000)
cache = {x : True for x in primes}
def is_prime(n):
	return n in cache

def is_truncatable(n):
	right = n // 10
	divident = 10
	while right:
		left = n % divident
		divident *= 10	
		#print('left is %d, right is %d' % (left, right))
		if not is_prime(left) or not is_prime(right):
			return False
		right =  right // 10
	return True

assert is_truncatable(3797)

result = []
for i in primes[4:]:
	if is_truncatable(i):
		result.append(i)
		if len(result) == 11:
			break

print(result)
print('sum is %d' % sum(result))


