def lattice_path(n):
  sum = 1
  for i in range(n + 1, 2 * n + 1):
    sum = sum * i
  for i in range(1, n + 1):
    sum = sum / i
  return sum

print(lattice_path(5))
