with open('p067_triangle.txt') as f:
  array = [[int(s) for s in line.split()] for line in f]

for i in range(len(array) - 2, -1, -1):
  for j in range(len(array[i])):
    array[i][j] = array[i][j] + max(array[i+1][j], array[i+1][j+1])

  print(array[i])
  
print(array[0][0])


