from typing import *
import sys

input = sys.stdin.readline

T : int = int(input())
for _ in range(T):
    N : int = int(input())
    arr = [input().rstrip() for _ in range(N)]

    result = []
    for i_1 in range(len(arr)):
        for i_2 in range(len(arr)):
            if i_1 == i_2: continue
            summ_string = arr[i_1] + arr[i_2]
            if summ_string == summ_string[::-1]:
                result.append(summ_string)

    if not result:
        print(0)
    else:
        print(result[0])