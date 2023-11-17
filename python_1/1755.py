from typing import *
import sys

input = sys.stdin.readline

data = {
    '0' : 'zero' ,
    '1' : 'one' ,
    '2' : 'two' ,
    '3' : 'three' ,
    '4' : 'four' ,
    '5' : 'five' ,
    '6' : 'six' ,
    '7' : 'seven' ,
    '8' : 'eight' ,
    '9' : 'nine'
}

M , N = map(int , input().split())
arr = []

for i in range(M , N + 1):
    if i < 10:
        arr.append([i , data[str(i)]])
    else:
        arr.append([i , data[str(i)[0]] + ' ' + data[str(i)[1]]])

arr = sorted(arr , key = lambda x : x[1])

for idx in range(len(arr)):
    if (idx + 1) % 10 == 0:
        print(f"{arr[idx][0]}")
    else:
        print(f"{arr[idx][0]}" , end = " ")