from typing import *
import sys

input = sys.stdin.readline

N , M = map(int , input().split())
arr = list(map(int , input().split()))
friends = list(map(int , input().split()))

idx = 0
count = 0
for f in friends:
    for i in range(len(arr)):
        if arr[i] == f and M <= i:
            if i == idx:
                idx += 1
            else:
                arr[i] , arr[idx] = arr[idx] , arr[i]
                count += 1
                idx += 1

print(count)