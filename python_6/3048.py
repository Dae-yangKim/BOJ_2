from typing import *
import sys

input = sys.stdin.readline

N , M = map(int , input().split())
g1 = list(input().rstrip())
g2 = list(input().rstrip())

g1 = g1[::-1] # 문자열 뒤집기
meet = g1 + g2 # 문자열 합치기

T : int = int(input())

for _ in range(T):
    for i in range(len(meet) - 1):
        if meet[i] in g1 and meet[i + 1] in g2:
            meet[i] , meet[i + 1] = meet[i + 1] , meet[i]

            if meet[i + 1] == g1[-1]:
                break

print("".join(meet))