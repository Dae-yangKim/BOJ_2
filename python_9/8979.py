from typing import *
import sys

input = sys.stdin.readline

N , M = map(int , input().split())
countries = []
for _ in range(N):
    arr = list(map(int , input().split()))
    countries.append(arr)

countries = sorted(countries , reverse = True , key = lambda x : (x[1] , x[2] , x[3]))

idx = [countries[i][0] for i in range(N)].index(M)

for i in range(N):
    if countries[idx][1:] == countries[i][1:]:
        print(i + 1)
        break