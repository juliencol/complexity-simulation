import time

def fibonacci2(n: int) -> int:
  memo = {0: 0, 1: 1}
  if n in memo:
    return memo[n]
  else:
    memo[n] = fibonacci2(n - 1) + fibonacci2(n - 2)
    return memo[n]
  
def get_runtime_of_fibonacci2(n: int) -> float:
  start1 = time.time()
  fibonacci2(n)
  stop1 = time.time()
  return (stop1 - start1) * (10 ** (3))

count = 0
fibonacci2_data = []
while count < 100:
  fibonacci2_data.append(get_runtime_of_fibonacci2(count))
  count += 5

print(fibonacci2_data)
