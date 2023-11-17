from typing import *
import sys

input = sys.stdin.readline

t : int = int(input())
input_arr = list(map(int , input().split()))

for i in range(t):
    if input_arr[i] == (int(input_arr[i] ** 0.5) ** 2):
        print(1 , end = " ")
    else:
        print(0 , end = " ")