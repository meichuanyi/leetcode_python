from math import ceil
T = int(input())
for _ in range(T):
    x, y, k = list(map(int, input().split()))
    a, b = ceil(x / k), ceil(y / k)
    if a > b:
        print(a * 2 - 1)
    else:
        print(a * 2)