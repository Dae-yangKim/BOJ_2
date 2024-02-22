from typing import *
import sys

input = sys.stdin.readline

N : int = int(input())
data = {}

for i in range(N):
    name , k , e , m = input().rstrip().split()
    
    if name not in data:
        data[name] = [int(k) , int(e) , int(m)]
    else:
        continue

data = sorted(data.items() , key = lambda x : (-x[1][0] , x[1][1] , -x[1][2] , x[0]))

for d in data:
    print(d[0])