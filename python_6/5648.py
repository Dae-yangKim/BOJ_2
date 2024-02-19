from typing import *
import sys

input = sys.stdin.readline

n , *arr = input().rstrip().split()
while len(arr) < int(n):
    data = input().rstrip().split()
    arr.extend(data)

result = [int(element[::-1] for element in arr)]
print(sorted(result , reverse = True) , sep = "\n")