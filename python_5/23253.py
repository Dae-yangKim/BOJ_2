from typing import *
import sys

input = sys.stdin.readline

N , M = map(int , input().split())
condi : bool = True
for i in range(M):
    n : int = int(input())
    arr = list(map(int , input().split()))
    for j in range(n - 1):
        if arr[j] < arr[j + 1]:
            condi = False
            break
    # False일 경우 , 이중 for문 탈출 필요
    if not condi:
        break
print("Yes" if condi else "No")