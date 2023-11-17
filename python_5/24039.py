from typing import *
import sys

input = sys.stdin.readline

S = []
num = 1

while num <= 120:
    for i in range(2 , num + 1):
        if num % i == 0:
            if num == i : S.append(i)
            break
    num += 1

i = 0
N = int(input())
while N >= (S[i] * S[i + 1]) : i += 1
print(S[i] * S[i + 1])