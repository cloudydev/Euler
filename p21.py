import math
def d(n):
	total = 1
	limit = math.sqrt(n)
	for i in range(2, int(limit + 1)):
		if n % i == 0:
			other = int(n / i)
			total += i if i >= other else i + other

	return total

limit = 10000
table = [d(n) for n in range(1, limit)]
t = 0
for i, v in enumerate(table, 1):
	if (v < limit):
		if table[v - 1] == i and v != i:
			print(i)
			t += i

print(t)




