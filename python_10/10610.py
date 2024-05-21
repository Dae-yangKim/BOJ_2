from typing import *
import sys

input = sys.stdin.readline 

N : str = input().rstrip()

if "0" not in N:
    print(-1)
else:
    summ : int = 0
    for i in range(len(N)):
        summ += int(N[i])
    
    if summ % 3 != 0:
        print(-1)
    else:
        sorted_num = sorted(N , reverse = True)
        answer = "".join(sorted_num)
        print(answer)