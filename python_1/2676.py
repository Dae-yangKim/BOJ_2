from typing import *
import sys

input = sys.stdin.readline

def solution(n : int , m : int) -> int:
    target : int = 1
    idx : int = 0

    if m == 0 or n == m:
        return 1
    
    for i in range(n - 1 , -(n - 1) - 1 , -2):
        if idx == m:
            return target
        target += i
        idx += 1


N : int = int(input())
for _ in range(N):
    n , m = map(int , input().split())
    print(solution(n , m))