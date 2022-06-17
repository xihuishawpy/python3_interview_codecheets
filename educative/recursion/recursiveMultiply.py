def recursive_multiply(x, y):
  return y if x == 1 else recursive_multiply(x - 1, y) + y