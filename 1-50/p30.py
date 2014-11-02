table = [pow(x, 5) for x in range(0, 10)]

def upper_limit():
    n = 1
    while n * table[9] / pow(10, n - 1) > 1:
        n = n + 1
    return 1 + (n - 1) * table[9]

def is_digit_fifth_pow(n):
    r = 1
    d = n
    digit_pow = 0
    while d:
        r = d % 10
        d = int(d / 10)
        digit_pow = digit_pow + table[r]

    return digit_pow == n
        
total = 0
for i in range(10, upper_limit()):
    if is_digit_fifth_pow(i):
        total = total + i

print(total)
