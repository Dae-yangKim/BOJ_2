from typing import *
import sys

input = sys.stdin.readline

N , K = map(int , input().split())
arr = [int(input()) for _ in range(N)]

length = N - K + 1

result = []
for idx in range(length):
    result.append(sum(arr[idx : idx + K]))

print(max(result))