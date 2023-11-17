from typing import *
import sys

input = sys.stdin.readline

def solution(N : int):
    stan : int = 9
    length : int = len(str(N))
    result : int = 0 #초기화
    
    if N < 10:
        return N
    else:
        for i in range(1 , length + 1):
            if i == length:
                result += (N - (10 ** (i - 1)) + 1) * i
            else:
                result += stan * 10 ** (i - 1) * i
        return result

N : int = int(input())
print(solution(N) % 1234567)