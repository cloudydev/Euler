def is_pandigital(a, b, n):
	used = [0 for x in range(0, 10)]
	str_n = str(a) + str(b) + str(n)

	for i in str_n:
		used[int(i)] += 1

	return all(used[1:]) and sum(used) == 9 and used[0] == 0


s = set()
# a * bcde = fghi
for i in range(2, 9 + 1):
	for j in range(1234, 9999 // 2):
		product = i * j
		if is_pandigital(i, j, product):
			print('%d * %d = %d' % (i, j, product))
			s.add(product)
			
# ab * cde = fghi
for i in range(12, 98 + 1):
	for j in range(123, 9999 // 12):
		product = i * j
		if is_pandigital(i, j, product):
			print('%d * %d = %d' % (i, j, product))
			s.add(product)

print(sum(s))