def sum_square_difference(n):
  list = [x * y for x in range(1, n + 1) for y in range(1, n + 1) if x != y]
  return sum(list)

print(sum_square_difference(100))
