#Spiral primes
import euler

side = 3
ratio = 1
primes = 0

while ratio >= 0.1:
	nth = (side + 1) // 2
	total = 4 * (nth - 1) + 1
	for i in range(4):
		n = side * side - i * (side - 1) 
		if euler.is_prime(n):
			primes += 1
	ratio = 1.0 * primes / total
	print(ratio)
	side += 2

print('solution: %d' % (side - 2))