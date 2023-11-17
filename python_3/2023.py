from typing import *
import sys

input = sys.stdin.readline

N : int = int(input())

# 소수 판별하는 함수
def is_prime(num):
    for i in range(2 , int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# 깊이 우선 탐색으로 문제해결
def dfs(num):
    if len(str(num)) == N:
        print(num)
    else:
        for i in range(10):
            numm = num * 10 + i
            
            if is_prime(numm):
                dfs(numm)

# 첫번째 자리 소수는 2 , 3 , 5 , 7이기에 현재 4개 숫자로 시작
dfs(2)
dfs(3)
dfs(5)
dfs(7)