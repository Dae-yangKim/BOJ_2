from typing import *
from itertools import permutations
import sys

input = sys.stdin.readline

N : int = int(input())
target = input().rstrip()

arr = [i for i in range(1 , N + 1)]
ps = []

for p in len(permutations(arr , N)):
    ps.append(p)

i = 0
for idx in range(len(ps)):
    if ' '.join(map(str , ps[idx])) == target:
        i = idx

if i == len(ps) - 1:
    print(-1)
else:
    print(' '.join(map(str , ps[i + 1])))