from typing import *
import sys

input = sys.stdin.readline

N : int = int(input())

if N % 2 == 0:
    print('SK')
else:
    print('CY')