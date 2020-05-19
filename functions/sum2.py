import time

def sum2(n: int) -> int:
  return n * (n + 1) / 2

def get_runtime_of_sum2(n: int) -> float:
  start1 = time.time()
  sum2(n)
  stop1 = time.time()
  return (stop1 - start1) * (10 ** (3))

count = 0
sum2_data = []
while count < 100:
  sum2_data.append(get_runtime_of_sum2(count))
  count += 5

print(sum2_data)

