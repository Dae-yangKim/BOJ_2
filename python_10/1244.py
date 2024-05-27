from typing import *
import sys

input = sys.stdin.readline

def solution(arr , s , idx):
    if s == 1: # 남성의 경우
        for i in range(idx - 1 , N , idx):
            if arr[i] == 1: arr[i] = 0
            else: arr[i] = 1
    else: # 여성의 경우
        n = min(idx - 1 , N - idx)
        if arr[idx - 1] == 0: arr[idx - 1] = 1
        else: arr[idx - 1] = 0
        for i in range(1 , n + 1):
            a , b = (idx - 1) - i , (idx - 1) + i
            if arr[a] == arr[b]:
                if arr[a] == 1: arr[a] = 0 ; arr[b] = 0
                else: arr[a] = 1 ; arr[b] = 1
            else: break

    return arr

N : int = int(input())
arr = list(map(int , input().split()))
R : int = int(input())
for _ in range(R):
    s , idx = map(int , input().split())
    arr = solution(arr , s , idx)

iiter : int = len(arr) // 20
namoji : int = len(arr) % 20

if iiter < 1:
    print(' '.join(map(str , arr)))
else:
    for i in range(iiter):
        print(' '.join(map(str , arr[i * 20 : i * 20 + 20])))
        if i == iiter - 1:
            print(' '.join(map(str , arr[i * 20 + 20 : i * 20 + 20 + (namoji - 1)])))

# 다른 블로그 정답
"""
def change(num):
    if switch[num] == 0:
        switch[num] = 1
    else:
        switch[num] = 0
    return


N = int(input())
switch = [-1] + list(map(int, input().split()))
students = int(input())
for _ in range(students):
    sex, num = map(int, input().split())
    # 남자
    if sex == 1:
        for i in range(num, N+1, num):
            change(i)
    # 여자
    else:
        change(num)
        for k in range(N//2):
            if num + k > N or num - k < 1 : break
            if switch[num + k] == switch[num - k]:
                change(num + k)
                change(num - k)
            else:
                break
                
for i in range(1, N+1):
    print(switch[i], end = " ")
    if i % 20 == 0 :
        print()
"""

"""
위처럼 조금 더 단순하게 코드를 짤 수 있어야 할 것 같다.
"""