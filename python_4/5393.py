from typing import *
import sys

input = sys.stdin.readline

def calc(num : int):
    data = {}
    count : int = 0
    for i in range(1 , num + 1):
        if i % 2 == 0 and (i // 2) not in data.values():
            data[i] = i // 2
            count += 1
        elif i % 2 != 0 and (3 * i + 1) not in data.values():
            data[i] = 3 * i + 1
            count += 1
        else:
            count -= 1
    
    return count

N : int = int(input())
for _ in range(N):
    num : int = int(input())
    k = calc(num)
    
    print(k)