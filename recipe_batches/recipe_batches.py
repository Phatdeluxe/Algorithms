#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  # get dictionaries
  if recipe.keys() != ingredients.keys():
    return 0
  # for each key
  batch = []
  for key in ingredients.keys():
  # interger divide owned value by recipe value
    quotient = ingredients[key] // recipe[key]
  # if quotient == 0 return cannot make
    if quotient <= 0:
      return 0
    else:
      batch.append(quotient)

  smallest_batch = batch[0]
  for size in batch:
    if size < smallest_batch:
      smallest_batch = size

  # return smallest quotient    
  return smallest_batch

# TODO: reflect

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))