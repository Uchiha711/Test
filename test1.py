n = int(input()) #changes only in uat
m = list(map(int,input().strip().split()))[:n]

a = min(m)

i = m.index(max(m))
m.pop(i)

b = max(m)

print(a*b)
