import math
last_ten = int(math.pow(10, 10))
def self_pow(n):
	result = 1
	for i in range(n):
		result *= n
		result %= last_ten
	return result

def solution(n):
	result = 0
	for i in range(1, n + 1):
		result += self_pow(i)
		result %= last_ten
	return result

print(solution(1000))