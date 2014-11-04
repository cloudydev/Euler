import euler

result = 0
for n in range(1, 101):
	for r in range(0, n + 1): 
		if euler.combinatoric_select(n, r) > 1000000:
			result += 1

print(result)


