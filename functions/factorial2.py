import time

def factorial2(n: int) -> int:
  result = 1
  while n > 1:
    result *= n
    n = n - 1
  return result

def get_runtime_of_factorial2(n: int) -> float:
  start1 = time.time()
  factorial2(n)
  stop1 = time.time()
  return (stop1 - start1) * (10 ** (3))

count = 0
factorial2_data = []
while count < 100:
  factorial2_data.append(get_runtime_of_factorial2(count))
  count += 5

print(factorial2_data)
