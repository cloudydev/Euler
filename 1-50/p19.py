offset =      [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
offset_leap = [31, 29, 30, 31, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(n):
  return n % 4 == 0 and n % 400 != 0

days = sum(offset_leap) if is_leap(1900) else sum(offset)
total = 0
for i in range(1901, 2001):
  o = offset_leap if is_leap(i) else offset
  for i in range(12):
    if days % 7 == 1:
      total = total + 1
    days += o[i]

print(total)
