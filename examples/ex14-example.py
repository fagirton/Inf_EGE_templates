n=9**8 + 3**5 - 9
c=0
while n>0:
  if n%3 == 2:
    c=c+1
  n=n//3
print(c)
