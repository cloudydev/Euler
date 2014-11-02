def palindrome(n):
  palindrome = 0
  while n:
    digit = n % 10
    n = n / 10
    palindrome = palindrome * 10
    palindrome = palindrome + digit

  return palindrome

def is_palindrome(n):
  return n == palindrome(n)

def max_palindrome():
  max_palindrome = 0
  for i in range(999, 99, -1):
    for j in range(999, 99, -1):
      n = i * j
      if is_palindrome(n):
        max_palindrome = max(n, max_palindrome)

  return max_palindrome

print(max_palindrome())
