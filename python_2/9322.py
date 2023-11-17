from typing import *
import sys

t = int(input())
for i in range(t):
	plain = []
	n = int(input())
	pub_1 = list(sys.stdin.readline().split())
	pub_2 = list(sys.stdin.readline().split())
	cyper = list(sys.stdin.readline().split())
	d = {}
	for j in pub_2:
		d[pub_1.index(j)] = cyper.pop(0)
	sorted_d = " ".join(dict(sorted(d.items())).values())
	print(sorted_d)