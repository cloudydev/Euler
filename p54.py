from euler import is_palindromic
from euler import reverse_digits

iterations = 50
def is_lychrel(d):
	for i in range(iterations):
		d = d + reverse_digits(d)
		if is_palindromic(d):
			return False
	return True

results = [x for x in range(1, 10001) if is_lychrel(x)]
print(len(results))