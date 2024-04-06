from typing import *
import sys

input = sys.stdin.readline

while True:
    N : int = int(input())
    if N == 0: break

    data = dict()
    for i in range(N):
        name , height = input().rstrip().split()
        if name not in data:
            data[name] = float(height)
        
    data = sorted(data.items() , reverse = True , key = lambda x : x[1])

    tall : float = 0
    for i in range(len(data)):
        print(data[i][0] , end = ' ')

        if (i + 1) != len(data) and data[i][1] > data[i + 1][1]:
            break