from typing import *
import sys

input = sys.stdin.readline

N , K = map(int , input().split())
arr = [int(input()) for _ in range(N)]

prefix_sum = [0] * (N + 1)
for i in range(N):
    prefix_sum[i + 1] = arr[i] + prefix_sum[i]

maxx : int = 0
for idx in range(K , N + 1):
    num : int = prefix_sum[idx] - prefix_sum[idx - K]
    if num > maxx: maxx = num

print(maxx)