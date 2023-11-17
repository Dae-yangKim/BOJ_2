from typing import *
import sys

input = sys.stdin.readline

def solution(idx):
    visited[idx] = True
    next_node = arr[idx]
    if not visited[next_node]:
        solution(next_node)
    return

T : int = int(input())
for _ in range(T):
    count : int = 0
    N : int = int(input())
    visited = [False] * (N + 1)
    arr = list(map(int , input().split()))
    arr.insert(0 , 0)

    for idx in range(1 , N + 1):
        if not visited[idx]:
            solution(idx)
            count += 1
    print(count)