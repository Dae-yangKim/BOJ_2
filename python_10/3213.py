from typing import *
import sys

input = sys.stdin.readline

N : int = int(input())
upper = [] ; under = []

for _ in range(N):
    n = list(input().rstrip().split("/"))
    
    upper.append(int(n[0])) ; under.append(int(n[1]))

maxx : int = max(under)

for idx in range(len(upper)):
    if under[idx] < maxx:
        num : int = maxx // under[idx]
        upper[idx] *= num

print(sum(upper) // maxx + 1)