f = open('p13.txt')
list = []

for line in f:
  list.append(int(line))

print(sum(list))
