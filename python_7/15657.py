from typing import *
import sys

input = sys.stdin.readline

def dfs(s):
    if len(temp) == M:
        print(*temp)
        return
    for i in range(s , N):
        temp.append(arr[i])
        dfs(i)
        temp.pop()

N , M = map(int , input().split())
arr = sorted(list(map(int , input().split())))
temp = []

dfs(0)