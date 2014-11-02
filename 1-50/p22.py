import math
def d(n):
	total = 1
	limit = math.sqrt(n)
	for i in range(2, int(limit + 1)):
		if n % i == 0:
			other = int(n / i)
			total += i if i >= other else i + other

	return total

limit = 28123
abundants  = [n for n in range(1, limit) if d(n) > n]
abundant_dict = {n : True for n in abundants}

def is_none_abundant_sum(n):
	for i in abundants:
		if i < n and n - i in abundant_dict:
			return False
	return True

print(sum(x for x in range(1, limit) if is_none_abundant_sum(x)))