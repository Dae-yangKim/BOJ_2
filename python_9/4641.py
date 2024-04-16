from typing import *
import sys

input = sys.stdin.readline

def solution(arr):
    count : int = 0
    for i in range(len(arr) - 1):
        if arr[i] * 2 in arr:
            count += 1
    
    return count

while True:
    arr = list(map(int , input().split()))
    if len(arr) == 1 and arr[0] == -1:
        break
    print(solution(arr))