from typing import *
import sys

input = sys.stdin.readline

def gcd(a , b):
    if b == 0 : return a
    return gcd(b , a % b)

a , b = map(int , input().split())

if a < b:
    a , b = b , a
    print((a * b) // gcd(a , b))
else:
    print((a * b) // gcd(a , b))