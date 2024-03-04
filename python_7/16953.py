from typing import *
from collections import deque
import sys

input = sys.stdin.readline

def bfs(N : int , M : int) -> int:
    q = deque([(N , 1)])
    visited = set()

    while q:
        current , count = q.popleft()

        if current == M:
            return count
        
        # 2를 곱한다
        double_current = current * 2
        if double_current not in visited and double_current <= M:
            visited.add(double_current)
            q.append((double_current , count + 1))
        
        # 1 추가
        append_current = int(str(current) + '1')
        if append_current not in visited and append_current <= M:
            visited.add(append_current)
            q.append((append_current , count + 1))
        
    # 변환 못함
    return -1

N , M = map(int , input().split())

print(bfs(N , M))