import string
import euler

with open('p042_words.txt') as f:
	words = [x.strip('"') for line in f for x in line.split(',')]

alpha_dict = {x : string.ascii_uppercase.index(x) + 1 for x in string.ascii_uppercase}

def word_value(word):
	return sum(alpha_dict[x] for x in word)

assert word_value('SKY') == 55
print(sum(1 if euler.is_triangle_number(word_value(x)) else 0 for x in words))