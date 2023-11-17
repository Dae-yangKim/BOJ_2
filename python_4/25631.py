from typing import *
import sys

N : int = int(input())
arr = list(map(int , input().split()))
data = {}

for a in arr:
    if a not in data:
        data[a] = 1
    else:
        data[a] += 1

count : int = 0
for val in data.values():
    if val > 1:
        count += 1

print(1 + count)