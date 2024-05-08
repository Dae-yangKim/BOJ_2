from typing import *
import sys

input = sys.stdin.readline 

R , C , zr , zc = map(int , input().split())
arr = [list(input().rstrip()) for _ in range(R)]

# zc 처리
for i in range(len(arr)):
    for j in range(len(arr[i])):
        arr[i][j] = arr[i][j] * zc

result = []
# zr 처리
for i in range(len(arr)):
    for _ in range(zr):
        result.append(arr[i])

for s in result:
    print(''.join(s))