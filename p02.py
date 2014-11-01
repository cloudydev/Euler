def even_sum(n):
  total = 0
  a, b = 1, 1

  while b < n:
    if b % 2 == 0:
      total = total + b
    a, b = b, a + b

  return total

print(even_sum(4000000))

