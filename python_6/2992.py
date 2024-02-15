from typing import *
import sys
import itertools

input = sys.stdin.readline

N = list(input().rstrip())
arr = list(itertools.permutations(N , len(N)))
arr.sort(reverse = True)

result = []
for s in arr:
    result.append("".join(s))

idx = result.index("".join(N))
print(result[idx - 1] if idx != 0 else 0)