import time

def fibonacci3(n: int) -> int:
  lastTwo = [0, 1]
  counter = 2
  while counter <= n:
    nextFib = lastTwo[0] + lastTwo[1]
    lastTwo[0] = lastTwo[1]
    lastTwo[1] = nextFib
    counter += 1
  return lastTwo[1] if n >= 1 else lastTwo[0]

def get_runtime_of_fibonacci3(n: int) -> float:
  start1 = time.time()
  fibonacci3(n)
  stop1 = time.time()
  return (stop1 - start1) * (10 ** (3))

count = 0
fibonacci3_data = []
while count < 100:
  fibonacci3_data.append(get_runtime_of_fibonacci3(count))
  count += 5

print(fibonacci3_data)
