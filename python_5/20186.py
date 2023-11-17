from typing import *
import sys

input = sys.stdin.readline

n , k = map(int , input().split())
arr = sorted(list(map(int , input().split())) , reverse = True)

result : int = 0
for i in range(k):
    result += arr[i] - i

print(result)