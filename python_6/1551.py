from typing import *
import sys

input = sys.stdin.readline

N , M = map(int , input().split())
arr = list(input().rstrip().split(','))

for idx in range(len(arr)):
    arr[idx] = int(arr[idx])

for _ in range(M):
    temp = []
    for i in range(len(arr) - 1):
        temp.append(arr[i + 1] - arr[i])
    arr = temp.copy()

if len(arr) == 1:
    print(str(arr[0]))
else:
    result = ','.join(map(str , arr))
    print(result)