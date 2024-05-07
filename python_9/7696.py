from typing import *
import sys

input = sys.stdin.readline

def solution(n : int):
    num : int = 1
    result : int = 1

    while True:
        if num == n:
            break

        s = str(result)
        if len(s) != 1 and len(s) > len(set(list(s))):
            result += 1
        else:
            num += 1
            result += 1

    return result 

while True:
    n : int = int(input())
    if n == 0: break

    print(solution(n))