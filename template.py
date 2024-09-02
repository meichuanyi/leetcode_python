from itertools import accumulate


# 求前缀和
numbers = [1, 2, 3, 4, 5]
result = list(accumulate(numbers, initial=0))
print(result)  # 输出: [0, 1, 3, 6, 10, 15]

# 邻接矩阵
n = 10
edges = [[0, 1]]
graph = [[] for _ in range(n)]
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)





