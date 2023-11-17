from typing import *
import sys

input = sys.stdin.readline

N : int = int(input())

if N == 1:
    print(4)
elif N == 2:
    print(6)
else:
    dp = [0] * (N + 1)

    dp[1] = 1
    dp[2] = 1
    for i in range(3 , N + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    result : int = dp[-1] * 2
    result += dp[N] + dp[N - 1]
    result += dp[N] + dp[N - 3] + dp[N - 2]

    print(result)