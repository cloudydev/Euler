import math

d = math.sqrt(2)
def is_right_triangle(a, b, c):
	return c > abs(a - b) and c < a + b and a * a + b * b == c * c

def solutions(n):
	result = 0
	upper = int(n / (d + 1)) + 1
	for a in range(1, upper):  
		for b in range(a, (n - a) // 2):
		 	if is_right_triangle(a, b, n - a - b):
		 		result += 1
	return result

n = 1000
total = 0
result = 0
assert solutions(120) == 3
for i in range(121, n + 1):
	s = solutions(i)
	#print('solution of %d is %d' % (i, s))
	if total < s:
		total = s
		result = i

print(result)


