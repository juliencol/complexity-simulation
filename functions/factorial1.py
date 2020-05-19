import time

def factorial1(n: int) -> int:
  if n == 0:
    return 1
  return n * factorial1(n - 1)

def get_runtime_of_factorial1(n: int) -> float:
  start1 = time.time()
  factorial1(n)
  stop1 = time.time()
  return (stop1 - start1) * (10 ** (3))

count = 0
factorial1_data = []
while count < 100:
  factorial1_data.append(get_runtime_of_factorial1(count))
  count += 5

print(factorial1_data)
