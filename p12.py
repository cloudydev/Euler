import math
import euler

array = euler.primes(2, 1000000)

def prime_factor(n, d):
    factor = 0
    while n % d == 0:
        n = n / d
        factor = factor + 1
    return factor

def divisible_number(n):
    total = 1
    for d in array:
        if d > n:
            break;
        factor = 1
        while n % d == 0:
            n = n / d
            factor = factor + 1
        total = total * factor
    return total

value = 1
i = 1
while divisible_number(value) <= 500:
    i = i + 1
    value = i * (i + 1) / 2
print(value)
