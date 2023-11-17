from typing import *
import math
import sys

input = sys.stdin.readline

def is_prime(num):
    if num == 0 or num == 1:
        return False
    for i in range(2 , int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

T : int = int(input())
for _ in range(T):
    num : int = int(input())
    while True:
        if is_prime(num):
            print(num)
            break
        num += 1