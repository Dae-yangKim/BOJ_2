from typing import *
import sys

input = sys.stdin.readline

N : int = int(input())

arr = [int(input()) for i in range(N)]
idx : int = 0
condition : bool = False

result : int = 0

while True:
    if arr[idx] >= arr[idx + 1]:
        result += arr[idx] - arr[idx + 1] +  1
        arr[idx ] = arr[idx + 1] - 1
        condition = True
    
    idx += 1
    
    if idx == len(arr) - 1:
        if condition:
            idx = 0 ; condition = False # 초기화
            continue
        else:
            break

print(result)