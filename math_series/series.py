def fibonacci(n):
  """
    Fibonacci Testing for Lab 2. This will be my interation version of fibonacci.
  """
  # pass
  seq_list = [0, 1]
  for i in range (2, n + 1):
      next_n = seq_list[-1] + seq_list[-2]
      seq_list.append(next_n)
  return seq_list[n - 1] 

def lucas(n):
  """
    Lucas Testing for Lab2. This will be my interation version of Lucas.
  """
  # pass
  seq_list = [2, 1]
  for i in range (2, n + 1):
      next_n = seq_list[-1] + seq_list[-2]
      seq_list.append(next_n)
  return seq_list[n - 1] 


def sum_series(n, first = 0, second = 1):
  """ 
    Sum Series for lab2. This will be my sum series, version of the equation. First argument is required, the second two are optional. First param will determine which element in the series to print. The two optional params will have default values of 0 and 1, and will determine the first two values for the series to be produced. 
  """ 
  # pass
  seq_list = [first, second]
  for i in range (2, n + 1):
      next_n = seq_list[-1] + seq_list[-2]
      seq_list.append(next_n)
  return seq_list[n - 1]
