n = (выражение) #в ячейке n лежит вычисленное выражение
c=0 #счётчик, пригодится позже
while n>0:
  if n%I == N:
    c=c+1 #добавляем к счётчику 1, если остаток от деления на I равен N
  n=n//I
print(c) #выводит, сколько раз программа видела N
