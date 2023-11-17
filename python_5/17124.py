

import sys

t = int(sys.stdin.readline())
# 이진탐색 함수 
def binary(i,B,start,end):
  diff = end - start
  if diff <= 1:
    return start
  mid = (start + end) // 2
  if i < B[mid]:
    return binary(i,B,start,mid)
  else:
    return binary(i,B,mid,end)

# 차이가 가장 작은 값의 인덱스를 반환
def findMin(c):
  curr = c[2]
  idx = 2
  if c[1] <= curr:
    curr = c[1]
    idx = 1
  if c[0] <= curr:
    curr = c[0]
    idx = 0
  return idx
 
for _ in range(t):
  # A의 총 개수 = n
  # B의 총 개수 = m
  n, m = map(int, sys.stdin.readline().split())
  A = list(map(int, sys.stdin.readline().split()))
  B = list(map(int, sys.stdin.readline().split()))
  B.sort()
  
  result = 0
  for i in A:
    p = binary(i,B,0,m)
    # p의 바로 앞, p, p의 바로 뒤 값
    diff = []
    diff.append(abs(B[p-1] - i))
    # A의 i값과 B배열에서 가장 가까운 값
    diff.append(abs(B[p] - i))
    diff.append(abs(B[(p+1) % m] - i))
    # 차이가 가장 작은 값의 인덱스
    idx = findMin(diff)
    result += B[p + idx - 1]
  print(result)