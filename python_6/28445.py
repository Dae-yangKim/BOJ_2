from typing import *
import sys

input = sys.stdin.readline

data = []

a , b = map(str , input().split())
c , d = map(str , input().split())

sett = set([a , b , c , d])

for s_1 in sett:
    for s_2 in sett:
        data.append([s_1 , s_2])

data = sorted(data , key = lambda x : (x[0] , x[1]))

for c_1 , c_2 in data:
    print(f"{c_1} {c_2}")