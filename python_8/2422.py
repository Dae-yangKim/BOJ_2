from typing import *
from itertools import combinations
import sys

input = sys.stdin.readline

N , M = map(int , input().split())
boolean_arr = [[False for _ in range(N)] for _ in range(N)]
for i in range(M):
    ban_1 , ban_2 = map(int , input().split())
    boolean_arr[ban_1 - 1][ban_2 - 1] = True
    boolean_arr[ban_2 - 1][ban_1 - 1] = True

count : int = 0

for c in combinations([i for i in range(1 , N + 1)] , 3):
    if boolean_arr[c[0] - 1][c[1] - 1] or boolean_arr[c[0] - 1][c[2] - 1] or boolean_arr[c[1] - 1][c[2] - 1]:
        continue
    count += 1

print(count)