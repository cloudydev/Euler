from fractions import gcd
d = 1
n = 1
for i in range(1, 10):
	for j in range(1, i):
		for k in range(1, j):
			if j * (10 * k + i) == k * (10 * i + j):
				n *= k
				d *= j

print(d // gcd(n, d))

