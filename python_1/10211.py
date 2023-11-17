from typing import *
import sys

input = sys.stdin.readline

T : int = int(input())
for _ in range(T):
    N : int = int(input())
    dp = [0] * N
    arr = list(map(int , input().split()))

    dp[0] = arr[0]
    for i in range(1 , len(arr)):
        dp[i] = max(arr[i] , arr[i] + dp[i - 1])
    
    print(max(dp))