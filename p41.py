import euler

# all other digit conbinatons except (1 .. 4) and （1 ... 7) can be divided evenly by 3
for i in reversed(euler.primes(7654321)):
	if euler.is_pandigital(i, 1, 7):
		print('largest pandigital prime is %d' % i)
		break

