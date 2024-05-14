from typing import *
import sys

input = sys.stdin.readline

N , S = map(int , input().split())
cows = sorted([int(input()) for _ in range(N)])

count : int = 0

start : int = 0
end : int = len(cows) - 1

while start < end:
    if cows[start] + cows[end] > S:
        end -= 1
    else:
        count += end - start
        start += 1

print(count)