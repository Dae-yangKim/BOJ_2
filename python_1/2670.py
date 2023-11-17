from typing import *
import sys

input = sys.stdin.readline

N : int = int(input())
dp = [float(input()) for _ in range(N)]

for i in range(1 , N):
    dp[i] = max(dp[i] , dp[i] * dp[i - 1])

print('{0:0.3f}'.format(max(dp)))