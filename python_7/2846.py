from typing import *
import sys

input = sys.stdin.readline

N : int = int(input())

length = []
arr = list(map(int , input().split()))

start = arr[0]

for idx in range(1 , len(arr)):
    if start < arr[idx] and arr[idx - 1] < arr[idx]:
        length.append(arr[idx] - start)
    else:
        start = arr[idx]

if length:
    print(max(length))
else:
    print(0)