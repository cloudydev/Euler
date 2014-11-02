def is_pandigital(n):
	used = [0 for x in range(0, 10)]
	str_n = str(n)
	for i in str_n:
		used[int(i)] += 1
	return all(used[1:]) and sum(used) == 9 and used[0] == 0

# the number should start with a digit 9
# 9x x (1, ..., n) generates (2, 3, ..., 3) digits number
# 9xx x (1, ..., n) generates (3, 4, ... , 4) digits number
# 9xxx x (1, ..., n) generates (4, 5, ..., 5) digits number 
# n > 1, so the fixed number must have 4 digits and n = 2

for i in range(9876, 9123 - 1, -1):
	s = str(i) + str(2 * i)
	if is_pandigital(s):
		print('%d x (1, 2) = %s' % (i, s))

