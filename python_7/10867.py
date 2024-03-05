from typing import *
import sys

input = sys.stdin.readline

N : int = int(input())
arr = sorted(list(set(list(map(int , input().split())))))

print(*arr)