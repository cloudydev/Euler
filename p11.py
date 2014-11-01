with open('p11.txt') as f:
  array = [[int(s) for s in line.split()] for line in f]

dim = len(array)
def sum_grid(i, j):
  right = array[i+1][j] * array[i+2][j] * array[i+3][j] if i < dim -3 else 0
  down = array[i][j+1] * array[i][j+2] * array[i][j+3] if j < dim -3 else 0 
  d1 = array[i+1][j+1] * array[i+2][j+2] * array[i+3][j+3] if i < dim -3 and j < dim - 3 else 0
  d2 = array[i-1][j+1] * array[i-2][j+2] * array[i-3][j+3] if i > 2 and j < dim - 3 else 0
  f = array[i][j]
  return max(max(f * right, f * d2), max(f * down, f * d1))


t = 0
for i in range(20):
  for j in range(20):
    t = max(t, sum_grid(i, j))

print(t)
