import math

digits = [x for x in range(0, 10)]

def nth_permutation(n):
	used_digits = {}
	result = []
	remain = n

	# total 10 digits
	for i in range(1, 11):
		t = math.factorial(10 - i) # max permutations with (10 - i) digits
		for d in [x for x in digits if x not in used_digits]:
			if remain > t:
				remain -= t
			else:
				used_digits[d] = True # find a digit!
				result.append(d)
				break
	return result

def sub_int(n, start):
	return n[start - 1] * 100 + n[start] * 10 + n[start + 1]

divident = [2, 3, 5, 7, 11, 13, 17]
def is_sub_divisible(n):
	return not any(sub_int(n, i) % divident[i - 2] for i in range(2, 9))

def list_to_int(l):
	result = 0
	scale = int(math.pow(10, 9))
	for i in range(10):
		result += scale * l[i]
		scale = scale // 10
	return result

assert is_sub_divisible([1,4,0,6,3,5,7,2,8,9])
assert list_to_int([1,4,0,6,3,5,7,2,8,9]) == 1406357289
#brute force solution
result = 0
for i in range(math.factorial(10)):
	l = nth_permutation(i)
	if is_sub_divisible(l):
		result += list_to_int(l)

print('solution is %d' % result)