from typing import *
from itertools import permutations
import sys

input = sys.stdin.readline

N , M = map(int , input().split())
arr = list(map(int , input().split()))

result = []
for s in permutations(arr , M):
    result.append(s)

result = sorted(result)

for s in result:
    print(" ".join(map(str , s)))