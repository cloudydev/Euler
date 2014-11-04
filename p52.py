from math import pow

def is_same_digits(a, b):
	s = [0 for x in range(10)]
	while a:
		r = a % 10
		t = b % 10
		s[r] += 1
		s[t] -= 1
		a = a // 10
		b = b // 10
	return all(not x for x in s)

assert is_same_digits(125874, 251748)

i = 1
found = False
# outer loop: number of digits
while not found:
	# x, 2x, ... 6x should have same digits, so upper bound is 10^i / 6
	for s in range(int(pow(10, i - 1)), int(pow(10, i)) // 6):
		if all(is_same_digits(s, j * s) for j in range(1, 7)):
			print('solution is : %d' % s)
			found = True
	i += 1
