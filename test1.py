n = int(input())
m = list(map(int,input().strip().split()))[:n] #changes only in dev

a = min(m)

i = m.index(max(m))
m.pop(i)

b = max(m)

print(a*b)
