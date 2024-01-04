from typing import *
import sys

input = sys.stdin.readline

def gcd(a : int , b : int):
    if b == 0: return a
    return gcd(b , a % b)

N : int = int(input())
for _ in range(N):
    arr = list(map(int , input().split()))
    result = []
    for i in range(len(arr)):
        for j in range(i + 1 , len(arr)):
            result.append(gcd(arr[i] , arr[j]))
    print(max(result))