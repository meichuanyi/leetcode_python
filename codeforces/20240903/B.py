T = int(input())
for _ in range(T):
    X = int(input())
    res = []
    for _ in range(X):
        tmp = input().index("#")
        res.append(int(tmp+1))
    print(res[::-1])
