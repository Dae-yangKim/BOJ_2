from typing import *
import sys

input = sys.stdin.readline

def solution(N : int) -> int:
    n = '1' * len(str(N))
    while True:
        if int(n) % N == 0:
            return len(n)
        else:
            n += '1'

while True:
    try:
        N : int = int(input())
        print(solution(N))
    except:
        break