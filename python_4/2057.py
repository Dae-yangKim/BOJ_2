def bf(now,i):
    if i==21:
        return now==n
    a=bf(now+fac[i],i+1)
    b=bf(now,i+1)
    return a or b
 
n=int(input())
if n==0:
    print("NO")
    exit()
fac=[1,1]
for i in range(2,21):
    fac.append(fac[-1]*i)
 
if bf(0,0):
    print("YES")
else:
    print("NO")