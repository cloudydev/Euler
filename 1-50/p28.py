def perimeter(level):
	return 1 if level == 1 else 4 * (2 * level - 1) - 4

def seed(level):
	return 0 if level == 1 else seed(level - 1) + perimeter(level - 1) + 5

max_level = (1001 + 1) // 2
print(1 + sum(4 * seed(i) for i in range(2, 1 + max_level)))
