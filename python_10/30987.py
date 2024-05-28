from typing import *
import sys

input = sys.stdin.readline

def f(a , b , c , x):
    return (a // 3) * (x ** 3) + (b // 2) * (x ** 2) + c * x 
    
def g(d , e , x):
    return (d // 2) * (x ** 2) + e * x

x1 , x2 = map(int , input().split())
a , b , c , d , e = map(int , input().split())

result = (f(a , b , c , x2) - g(d , e , x2)) - (f(a , b , c , x1) - g(d , e , x1))

print(result)