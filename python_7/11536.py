from typing import *
import sys

input = sys.stdin.readline

N : int = int(input())
name = []
for i in range(N):
    name.append(input().rstrip())

if sorted(name) == name:
    print('INCREASING')
elif sorted(name , reverse = True) == name:
    print('DECREASING')
else:
    print('NEITHER')