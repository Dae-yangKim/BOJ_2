from typing import *
import sys

input = sys.stdin.readline

R , G , B = map(int , input().split())
count : int = 0

# 3개 다른 색
while True:
    if 0 in [R , G , B]: break
    R -= 1 ; G -= 1 ; B -= 1
    count += 1

