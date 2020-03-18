#!/usr/bin/python

import argparse

def find_max_profit(prices):
  # get a list of ints (prices)
  # starting with the first value iterate through the list
  k = 1
  diff = []
  for i in range(len(prices)):
    # stop when last value is reached
    if i == len(prices) - 1:
      break
    
    for j in range(k, len(prices)):
    # dont compare the same value
    # dont compare previous values
    # store differences of all following values
      diff.append([prices[i], prices[j], prices[j] - prices[i]])
    k += 1    
  # comapre stored differences
  largest_dif = diff[0][2]
  for value in diff:
    if value[2] > largest_dif:
      largest_dif = value[2]
  # return largest difference
  return largest_dif
    # TODO: Figure out how to format the return


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
  

  #TODO: Reflect!!!
