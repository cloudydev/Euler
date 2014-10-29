import math
def is_prime(n):
	if n <= 0:
		return False
	if n % 2 == 0 and n > 2:
		return False
	return all(n % i for i in range(3, int(math.sqrt(n) + 1), 2))

def equation(x, a, b):
	return x * x + a * x + b

def consecutive_prime_len(a, b):
	i = 0
	while is_prime(equation(i, a, b)):
		i += 1
	return i

assert consecutive_prime_len(-79, 1601) == 80
assert consecutive_prime_len(1, 41) == 40

limit = 1000
max_len = 0
max_product = 0

# b must be a prime

for b in [x for x in range(2, limit) if is_prime(x)]:
	for a in range(-limit + 1, limit):
		if equation(max_len, a, b) <= 0:
			continue
		l = consecutive_prime_len(a, b)
		if max_len < l:
			max_len = l
			max_product = a * b

print('max product is %d, max length is %d' % (max_product, max_len))