from typing import *
import sys

input = sys.stdin.readline

N : int = int(input())
arr = list(map(int , input().split()))

sum_nums = sum(arr)
result : int = 0

for n in arr:
    sum_nums -= n
    result += sum_nums * n

print(result)