N = int(input())
li = sorted(map(int, input().split()))
res = 0
for i in range(N-1):
    s, e = i+1, N-1
    t = -1
    while s <= e:
        m = (s+e)//2
        if li[i] >= 0.9*li[m]:
            t = m
            s = m+1
        else:
            e = m-1
    res += t-i if t > -1 else 0
print(res)