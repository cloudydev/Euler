import math

def is_prime(n):
  if n % 2 == 0 and n > 2:
    return False

  return all(n % i for i in range(3, 1 + int(math.sqrt(n)), 2))

def summation_of_primes_below(n):
  return sum([x for x in range(2, n) if is_prime(x)])

print(summation_of_primes_below(2000000))
