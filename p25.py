list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

while len(str(list[-1])) < 1000:
  list.append(list[-1] + list[-2])

print(len(list))
