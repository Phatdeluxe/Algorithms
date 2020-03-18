#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
  permutations_found = 0
  # base case n == 1
  if n < 0:
    return 0
  if n == 0:
    return 1
  # subtract 1 from n
  permutations_found += eating_cookies(n-1)
  # subtract 2 from n
  permutations_found += eating_cookies(n-2)
  # subtract 3 from n
  permutations_found += eating_cookies(n-3)

  return permutations_found


# thinking some massive for loops
  # base case, n > 0
  # int division by 3
    # for i in range(3quotient)
      # n - (3 * i)
      # int division by 2
        # for j in range(2quotient)
        # n - (2 * 2quotient)
          # remaining n is the number of 1s
            # permutations += 1
  # int division by 2
    # for i in range(2Quotient)
      # n - (2 * i)
      # remaining is 1
        # permutations += 1
  # remaining n is the number of 1s


def eating_cookies1(n, cache=None):
  cookies_left = n
  permutations = 0
  quotient3 = 0
  quotient2 = 0
  if n < 0:
    return 0
  elif n == 0:
    return 1
  else:
      
    quotient3 = n // 3
    for i in range(quotient3 + 1):
      cookies_left = n - (3 * i)
      if cookies_left < 0:
        continue
      elif cookies_left == 0:
        permutations += 1
      else:
        quotient2 = cookies_left // 2
        for j in range(quotient2 + 1):
          cookies_left = n - ((2 * j) + (3 * i))
          if cookies_left < 0:
            continue
          elif cookies_left == 0:
            permutations += 1 + i
          elif i > 0 or j > 0:
            permutations += cookies_left + i + j
          else:
            permutations += 1
    
    return permutations

eating_cookies(10)

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')






# 5
# 3, 2 | 2, 3
# 3, 1, 1 | 1, 3, 1 | 3, 1, 1
# 2, 2, 1 | 2, 1, 2 | 1, 2, 2
# 2, 1, 1, 1 | 1, 2, 1, 1 | 1, 1, 2, 1 | 1, 1, 1, 2
# 1, 1, 1, 1, 1


# 10
# 3, 2, 2, 1, 1, 1