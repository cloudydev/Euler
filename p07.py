import euler

current = 104729
while True:
  current = current + 2
  if euler.is_prime(current):
    print(current)
    break
