def is_triplet(a, b, c):
  return a * a + b * b == c * c


list = [[a, b, c] 
    for a in range(1, 1001) 
    for b in range(a + 1, 1001) 
    for c in range(1000 - a - b, 1000 - a - b + 1)
    if c > abs(a - b) and c < (a + b) and is_triplet(a, b, c)]

s = list[0]
print(s[0] * s[1] * s[2])
