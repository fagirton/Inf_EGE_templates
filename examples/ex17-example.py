with open("17.txt", 'r') as f:
  a=[int(x) for x in f.read().splitlines()] 
с = 0
m = 0
for i in range(len(a) - 1):
    for j in range(i + 1, len(a)):
        if (a[i] % 160 != a[j] % 160) and ((a[i] % 7 == 0) or (a[j] % 7 == 0)):
            с += 1
            m = max(mx, a[i] + a[j])
print(с, m)
