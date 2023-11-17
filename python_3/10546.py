from typing import *
import sys

input = sys.stdin.readline

N : int = int(input())
data = {}

for _ in range(N):
    name = input().rstrip()
    if name not in data:
        data[name] = 1
    else:
        data[name] += 1

for _ in range(N - 1):
    name = input().rstrip()
    data[name] -= 1

for name in data.keys():
    if data[name] > 0:
        print(name)