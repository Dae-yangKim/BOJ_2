from typing import *
import sys

input = sys.stdin.readline

T : int = int(input())
for _ in range(T):
    usr : str = input().rstrip()
    pwd = []
    sub = []

    for x in usr:
        if x == "<":
            if pwd:
                sub.append(pwd.pop())
        elif x == ">":
            if sub:
                pwd.append(sub.pop())
        elif x == "-":
            if pwd:
                pwd.pop()
        else:
            pwd.append(x)
    
    print("".join(pwd) , "".join(sub[::-1]) , sep = "")