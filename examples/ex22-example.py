for i in range(0,10000):
  x = i
  a, b = 0, 0
  while x > 0:
      a = a + 1
      b = b + x%100
      x = x//100
  if a==2 and b==13: print(i)
