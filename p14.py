import time
import operator
cache = {1:0, 2:1}

def chain_length(n):
  length = 0
  i = n
  
  while i != 1 and i not in cache:    
    length = length + 1
    i = 3 * i + 1 if i % 2 else i / 2

  cache[n] = cache[i] + length
  return cache[n]
 
def solution(n):
  max = 0
  j = 0
  for i in range(1, n + 1):
    l = chain_length(i)
    if max < l:
      max = l
      j = i
  return j

start = time.time()
print(solution(1000000))
print(time.time() - start)
