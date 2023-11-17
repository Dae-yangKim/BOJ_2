from typing import *
import sys

input = sys.stdin.readline

def solution(k : int):
    
    value_1 = a * k + b
    value_2 = c * k + d

    if value_1 == value_2:
        return True , value_1
    else:
        return False , None

k : int = int(input())
a , b , c , d = map(int , input().split())

condition , value = solution(k)

if condition:
    print(f"Yes {value}")
else:
    print("No")