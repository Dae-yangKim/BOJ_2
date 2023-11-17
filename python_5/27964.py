from typing import *
from collections import defaultdict
import sys

input = sys.stdin.readline

data = defaultdict(int)

N : int = int(input())
ingredients = input().rstrip().split()

count : int = 0

for ig in ingredients:
    if ig[-6:] == 'Cheese':
        if ig not in data:
            count += 1
            data[ig] = 1
        else:
            data[ig] += 1

if count >= 4:
    print('yummy')
else:
    print('sad')