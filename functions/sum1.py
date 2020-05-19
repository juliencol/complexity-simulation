import time

def sum1(n: int) -> int:
  total = 0
  for i in range(n + 1):
    total += i
  return total

def get_runtime_of_sum1(n: int) -> float:
  start1 = time.time()
  sum1(n)
  stop1 = time.time()
  return (stop1 - start1) * (10 ** (3))

count = 0
sum1_data = []
while count < 100:
  sum1_data.append(get_runtime_of_sum1(count))
  count += 5

print(sum1_data)


