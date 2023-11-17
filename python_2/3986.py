from typing import *
import sys

input = sys.stdin.readline

stack = []

N : int = int(input())
arr = [input().rstrip() for _ in range(N)]
count : int = 0

for sentence in arr:
    for s in sentence:
        if not stack:
            stack.append(s)
        else:
            stack.append(s)
            
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
    
    if not stack:
        count += 1
    stack = []

print(count)