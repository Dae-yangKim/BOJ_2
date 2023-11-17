from typing import *
import sys

input = sys.stdin.readline

T : int = int(input())
for _ in range(T):
    arr = input().rstrip().split()
    data = {}
    while True:
        usrInput = input().rstrip()
        if usrInput == "what does the fox say?":
            break
        usrInput = usrInput.split()
        data[usrInput[0]] = usrInput[2]
    
    for s in arr:
        if s not in data.values():
            print(s , end = " ")