from typing import *
import sys

input = sys.stdin.readline

def median(arr):
    sorted_arr = sorted(arr)
    length = len(sorted_arr)

    if length % 2 == 1:
        return sorted_arr[length // 2]
    else:
        mid1 = sorted_arr[length // 2 - 1]
        mid2 = sorted_arr[length // 2]
        return (mid1 + mid2) / 2

def solution(arr , r , c):
    result = []
    for i in range(r):
        median_arr = []
        for j in range(c):
            sub = [row[j : j + 3] for row in arr[i : i + 3]]
            flattened_list = [item for sublist in sub for item in sublist]
            median_arr.append(median(flattened_list))
        result.append(median_arr)
    
    return result

R , C = map(int , input().split())
arr = [list(map(int , input().split())) for _ in range(R)]
T = int(input())

arr = solution(arr , R - 2 , C - 2)

count : int = 0
for s in arr:
    for n in s:
        if n >= T:
            count += 1

print(count)