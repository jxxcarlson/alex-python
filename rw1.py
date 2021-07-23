import random

# Random number generator
# Calling rand returns a random
# number in the range [0, 1]
def step():
    return 2*random.random() - 1

steps = 10

position = 0.0
for tick in range(0, steps):
    position = position + step()

print position


