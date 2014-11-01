def sum(total, n):
  num = (total - 1) // n
  return n * num * (num + 1) // 2;


total = 1000
print(sum(total, 3) + sum(total, 5) - sum(total, 3 * 5))

