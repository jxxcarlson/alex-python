# File: rw2.py
import random

# Random number generator
# Calling step returns a random
# number in the range [-1, 1]
def step():
    return 2*random.random() - 1

def randomWalk(initialPosition, steps):
  position = initialPosition
  for tick in range(0, steps):
    position = position + step()
  return position

for i in range(0, 20):
  print i + 1, randomWalk(0, 1000)