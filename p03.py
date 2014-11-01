import math

def max(a, b):
  if a > b:
    return a
  return b

def is_prime(n):
  if n % 2 == 0 and n > 2:
    return False

  return all(n % i for i in range(3, int(math.sqrt(n)), 2))

def max_prime_factor(n):
  if n == 2:
    return n

  total = int(math.sqrt(n))
  
  for i in range(2, total):
    if n % i == 0:
      other = n / i
      if is_prime(i) and is_prime(other):
        return max(i, other)
      else:
        return max(max_prime_factor(n / i), max_prime_factor(i))

  return 1

print(max_prime_factor(600851475143))
