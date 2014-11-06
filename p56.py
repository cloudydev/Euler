# Powerful digit sum
max_sum = 0
for a in range(1, 100):
	digits = [1]
	for b in range(1, 100):
		remainder = 0
		for i in range(len(digits)):
			p = digits[i] * a + remainder
			digits[i] = p % 10
			remainder = p // 10
		while remainder:
			digits.append(remainder % 10)
			remainder = remainder // 10
		s = sum(digits)
		if max_sum < s:
			max_sum = s

print(max_sum)