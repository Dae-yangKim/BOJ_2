from typing import *
import sys

input = sys.stdin.readline

N : int = int(input())
sentence : str = input().rstrip()

holder : int = 0
for s in sentence:
    if s == 'S': holder += 2
    else: holder += 1

H : int = holder - (sentence.count('S') - 1) - (sentence.count('L') // 2)

if H <= len(sentence):
    print(H)
else:
    print(len(sentence))