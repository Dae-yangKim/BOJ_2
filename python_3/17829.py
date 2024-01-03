from typing import *
import sys

input = sys.stdin.readline

def d_a_q(N : int , arr):
    if N == 2:
        flattenend = [value for sub in arr for value in sub]

        return sorted(flattenend , reverse = True)[1]        
    else:
        n = N // 2
        v1 = d_a_q(n , [row[:n] for row in arr[:n]])
        v2 = d_a_q(n , [row[n : N] for row in arr[:n]])
        v3 = d_a_q(n , [row[:n] for row in arr[n : N]])
        v4 = d_a_q(n , [row[n : N] for row in arr[n : N]])

        answer = [v1 , v2 , v3 , v4]
        answer.sort()
        return answer[-2]
N : int = int(input())
arr = [list(map(int , input().split())) for _ in range(N)]

print(d_a_q(N , arr))