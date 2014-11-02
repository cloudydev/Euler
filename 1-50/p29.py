import math
print(len({math.pow(i, j) : True for i in range(2, 101) for j in range(2, 101)}))