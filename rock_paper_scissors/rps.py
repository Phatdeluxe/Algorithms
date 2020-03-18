#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  rps = []
  if n <= 0:
    return [[]]
  else:
    rps = add_moves(rps, n)

  return rps
  # recurse
  # return list of results


def add_moves(arr, n):
  if n == len(arr):
    return [arr]
  else:
    arr += add_moves(arr + ['rock'], n)
    arr += add_moves(arr + ['paper'], n)
    arr += add_moves(arr + ['scissors'], n)
    return arr

rock_paper_scissors(2)

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')