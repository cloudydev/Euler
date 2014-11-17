#Square root convergents
from euler import digit_length

#[numerator, denominator]
expansions = [[3, 2]]

for i in range(999):
	last = expansions[-1]
	expansions.append([last[0] + 2 * last[1], last[0] + last[1]])

print(len([1 for x in expansions if digit_length(x[0]) > digit_length(x[1])]))