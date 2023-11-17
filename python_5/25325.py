from typing import *
from collections import defaultdict
import sys

input = sys.stdin.readline
data = defaultdict(int)

N : int = int(input())
names = list(input().rstrip().split())

for name in names:
    data[name] = 0 # 초기화

for i in range(N):
    A = list(input().rstrip().split())
    for name in A:
        if name == names[i]: continue
        data[name] += 1

data = sorted(data.items() , key = lambda x : (-x[1] , x[0]))

for d in data:
    print(f"{d[0]} {d[1]}")