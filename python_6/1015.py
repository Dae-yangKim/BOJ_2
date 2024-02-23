from typing import *
import sys

input = sys.stdin.readline

N : int = int(input())
A = list(map(int , input().split()))
temp = A.copy()
A = sorted(A)

data = {}
idx : int = 0
for i in range(len(A)):
    if A[i] not in data:
        data[A[i]] = [idx]
    else:
        data[A[i]].append(idx)
    idx += 1

result = []
for s in temp:
    result.append(data[s][0])
    data[s].pop(0)

print(' '.join(map(str , result)))