sentence = []
N = int(input())

for _ in range(N):
    s = list(input().rstrip().split())
    for idx in range(len(s)):
        s[idx] = s[idx][::-1]
    sentence.append(s)

for s in sentence:
    print(" ".join(s))