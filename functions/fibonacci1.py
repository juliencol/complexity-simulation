import time

def fibonacci1(n: int) -> int:
  if n == 0: return 0
  if n == 1: return 1
  return fibonacci1(n - 1) + fibonacci1(n - 2)

def get_runtime_of_fibonacci1(n: int) -> float:
  start1 = time.time()
  fibonacci1(n)
  stop1 = time.time()
  return (stop1 - start1) * (10 ** (3))

count = 0
fibonacci1_data = []
while count < 100:
  fibonacci1_data.append(get_runtime_of_fibonacci1(count))
  count += 5

print(fibonacci1_data)
