from typing import *
import sys

input = sys.stdin.readline

s : str = input().rstrip()
arr = []

for i in range(len(s) - 2):
    for j in range(i + 1 , len(s) - 1):
        for k in range(j + 1 , len(s)):
            sentence = s[:j][::-1] + s[j:k][::-1] + s[k:][::-1]
            arr.append(sentence)

print(min(arr))