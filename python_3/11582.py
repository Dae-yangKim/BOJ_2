from typing import *
import sys

input = sys.stdin.readline

def divide_and_conquer(divid : int):
    d : int = N // divid
    for i in range(d):
        arr[i * divid : (i + 1) * divid] = sorted(arr[i * divid : (i + 1) * divid])
    if d == k:
        for num in arr:
            print(num , end = ' ')
        sys.exit(0)
    divide_and_conquer(divid * 2)

N : int = int(input())
arr = list(map(int , input().split()))
k : int = int(input())

divide_and_conquer(2)