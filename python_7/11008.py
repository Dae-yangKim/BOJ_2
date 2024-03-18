N : int = int(input())
for _ in range(N):
    sentence = input().rstrip().split()
    s , p = sentence[0] , sentence[1]
    
    count = s.count(p)
    print(len(s) - (count * len(p)) + count)