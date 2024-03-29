from typing import *
from itertools import permutations
import sys

input = sys.stdin.readline

while True:
    try:
        s , N = map(str , input().rstrip().split())
        count = 0
        condition = True
        for p in permutations(s):
            count += 1
            if count == int(N):
                print(f"{s} {N} = {''.join(p)}")
                condition = False ; break
        
        if condition:
            print(f"{s} {N} = No permutation")
    except:
        break