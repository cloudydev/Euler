def factor(n):
	t = 1
	for i in range(1, n + 1):
		t *= i
	return t

def nth(n):
	digits = [x for x in range(0, 10)]
	used_digits = {}
	result = []
	remain = n
	# total 10 digits
	for i in range(1, 11):
		t = factor(10 - i) # max permutations with (10 - i) digits
		for d in [x for x in digits if x not in used_digits]:
			if remain > t:
				remain -= t
			else:
				used_digits[d] = True # find a digit!
				result.append(d)
				break
	return result

print(nth(1000000 ))