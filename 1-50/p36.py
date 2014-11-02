import math
def is_palindromw_10(n):
	t = 0
	old_n = n
	while n:
		t *= 10
		t += n % 10
		n = n // 10

	return t == old_n

def reverse_2(n):
	bit_len = int(math.log(n, 2)) + 1
	u = 0
	for i in range(1, bit_len + 1):
		u += (n & 1) << (bit_len - i)
		n = n >> 1
	return u

def is_palindromw_2(n):
	return n == reverse_2(n)

assert is_palindromw_10(585)
assert is_palindromw_2(585)


result = [x for x in range(1, 1000000) if is_palindromw_10(x) and is_palindromw_2(x)]
print(result)
print(sum(result))