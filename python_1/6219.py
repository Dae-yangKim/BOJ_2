from typing import *
import sys

input = sys.stdin.readline

def eratos_solution(A : int , B : int):
    primes = [True] * (B + 1)

    m = int((B + 1) ** 0.5)
    for i in range(2 , m + 1):
        if primes[i] == True:
            for j in range(i + i , (B + 1) , i):
                primes[j] = False
    
    return [i for i in range(2 , (B + 1)) if primes[i] == True]

A , B , C= map(int , input().split())
result = eratos_solution(A , B)
count : int = 0

for num in result:
    if num >= A and str(C) in str(num):
        count += 1

print(count)