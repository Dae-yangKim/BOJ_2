from typing import *
import sys

input = sys.stdin.readline

def calculate_sum(n, x):
    total_sum = sum(x)
    square_sum = sum(xi ** 2 for xi in x)
    result = (total_sum ** 2 - square_sum) // 2
    return result

# 입력을 받아서 처리
n = int(input())
x = list(map(int, input().split()))

# 결과 계산 및 출력
print(calculate_sum(n, x))