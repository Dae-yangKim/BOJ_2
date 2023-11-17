from typing import *
import sys

input = sys.stdin.readline

N : int = int(input())
dp = [0] * (N + 1)

if N < 4:
    print(1)
else:
    dp[1] = 1 ; dp[2] = 1 ; dp[3] = 1

    for i in range(4 , N + 1):
        dp[i] = dp[i - 1] + dp[i - 3]

    print(dp[N])