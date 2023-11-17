from typing import *
import sys

input = sys.stdin.readline

while True:
    factorial : int = 1
    idx : int = 0

    try:
        N : int = int(input())
        while idx != N:
            idx += 1
            factorial *= idx
        
        while True:
            condi : int = factorial % 10
            if condi:
                break
            factorial //= 10
        
        print(f"{N:5} -> {condi}")
    except:
        break